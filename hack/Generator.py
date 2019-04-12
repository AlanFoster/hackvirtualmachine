from typing import Any, List, Callable


def push_operation(operation: Callable[..., List[str]]) -> Callable[..., str]:
    """
    Pushes the current value assigned to the D register onto the stack
    """

    def wrapper(*args: Any, **kwargs: Any) -> str:
        return "\n".join(
            operation(*args, **kwargs)
            + [
                # *sp = d
                "@SP",  # Fetch the segment pointer
                "A=M",  # Load *sp into the address register
                "M=D",  # *sp = D
                # Increment stack, sp++
                "@SP",
                "M=M+1",
            ]
        )

    return wrapper


def pop_operation(operation: Callable[..., List[str]]) -> Callable[..., str]:
    def wrapper(*args: Any, **kwargs: Any) -> str:
        return "\n".join(
            [
                # Decrement stack, sp--
                "@SP",
                "AM=M-1",
                "D=M",
            ]
            + operation(*args, **kwargs)
        )

    return wrapper


def unary_operation(operation: Callable[..., List[str]]) -> Callable[..., str]:
    """
    Replaces the top value on the stack with the given computation
    """

    def wrapper(*args: Any, **kwargs: Any) -> str:
        return "\n".join(
            # fmt: off
            [
                "@SP",
                "A=M-1",
            ] + operation(*args, **kwargs)
            # fmt: on
        )

    return wrapper


def binary_operation(operation: Callable[..., List[str]]) -> Callable[..., str]:
    """
    Pop the top two values from the stack, and push the given binary computation result back onto the stack.
    """

    def wrapper(*args: Any, **kwargs: Any) -> str:
        return "\n".join(
            # fmt: off
            [
                # SP--
                "@SP",
                "AM=M-1",

                # Store *sp within D
                "D=M",

                # Set address register to second number
                "A=A-1",
            ] +
            # fmt: on
            operation(*args, **kwargs)
        )

    return wrapper


def pointer_name(pointer: str) -> str:
    pointer_labels = {"0": "THIS", "1": "THAT"}
    if pointer not in pointer_labels:
        raise ValueError(
            f'Pointer target may only be 0 (THIS) or 1 (THAT), instead received "{pointer}"'
        )
    return pointer_labels[pointer]


def temp_register(i: str) -> int:
    temp_registers_start = 5
    temp_registers_end = 12
    allocated_register = temp_registers_start + int(i)

    if allocated_register > temp_registers_end:
        raise ValueError(
            f'Unexpected temp register value: "{allocated_register}". This would cause overflow. '
            f"Available registers: R{temp_registers_start}-R{temp_registers_end}"
        )

    return allocated_register


class Generator:
    # Mapping human readable virtual machine names to the hack assembly labels
    hack_segment_labels = {
        "local": "LCL",
        "argument": "ARG",
        "this": "THIS",
        "that": "THAT",
    }

    # Mapping
    # fmt: off
    comparison_operators = {
        "eq": "JEQ",
        "gt": "JGT",
        "lt": "JLT"
    }

    # fmt: on

    def __init__(self, namespace: str) -> None:
        self.namespace = namespace
        self.comparison_count = 0
        self.call_count = 0

    def bootstrap(self) -> str:
        return "\n".join(
            [
                "// Bootstrap",
                # SP = 256
                "@256",
                "D=A",
                "@SP",
                "M=D",
                # Call Sys.int
                self.call("Sys.init", 0),
            ]
        )

    @push_operation
    def push_static(self, i: int) -> List[str]:
        return [
            # Load global address
            f"@{self.namespace}.{i}",
            "D=M",
        ]

    @push_operation
    def push_constant(self, value: str) -> List[str]:
        return [
            # Set constant in stack pointer
            f"@{value}",
            "D=A",
        ]

    @push_operation
    def push_segment_value(self, name: str) -> List[str]:
        # fmt:off
        return [
            f"@{name}",
            "D=M",
        ]
        # fmt:on

    @push_operation
    def push_pointer(self, pointer: str) -> List[str]:
        # fmt:off
        return [
            f"@{pointer_name(pointer)}",
            "D=M",
        ]
        # fmt:on

    @push_operation
    def push_segment(self, segment: str, i: int) -> List[str]:
        return [
            # Calculating addr, where addr = LCL + i
            f"@{self.hack_segment_labels[segment]}",  # Load the value stored in segment
            "D=M",
            f"@{i}",  # Load i
            "A=D+A",  # Set address register to addr
            "D=M",  # Load the value stored within addr, i.e. *addr
        ]

    @push_operation
    def push_temp(self, i: str) -> List[str]:
        return [f"@{temp_register(i)}", "D=M"]

    @binary_operation
    def comparison_operator(self, operator: str) -> List[str]:
        self.comparison_count += 1
        jump_name = self.comparison_operators[operator]

        # fmt: off
        return [
            # Subtract both numbers
            "D=M-D",

            # Jumping logic
            f"@{jump_name}.True.{self.comparison_count}",
            f"D;{jump_name}",

            # False path
            f"({jump_name}.False.{self.comparison_count})",
            "D=0",
            f"@{jump_name}.Finally.{self.comparison_count}",
            f"0;JMP",

            # True Path
            f"({jump_name}.True.{self.comparison_count})",
            "D=-1",

            f"({jump_name}.Finally.{self.comparison_count})",

            "@SP",
            "A=M-1",
            "M=D"
        ]
        # fmt: on

    @binary_operation
    def sub(self) -> List[str]:
        return ["M=M-D"]

    @binary_operation
    def add(self) -> List[str]:
        return ["M=M+D"]

    @unary_operation
    def neg(self) -> List[str]:
        return ["M=-M"]

    @binary_operation
    def logical_and(self) -> List[str]:
        return ["M=D&M"]

    @binary_operation
    def logical_or(self) -> List[str]:
        return ["M=D|M"]

    @unary_operation
    def logical_not(self) -> List[str]:
        return ["M=!M"]

    @pop_operation
    def pop_temp(self, i: str) -> List[str]:
        return [
            # Store the new value
            f"@{temp_register(i)}",
            "M=D",
        ]

    @pop_operation
    def pop_pointer(self, pointer: str) -> List[str]:
        return [
            # Store the new value
            f"@{pointer_name(pointer)}",
            "M=D",
        ]

    @pop_operation
    def pop_static(self, i: int) -> List[str]:
        return [
            # Store the new value
            f"@{self.namespace}.{i}",
            "M=D",
        ]

    def pop_segment(self, segment: str, i: int) -> str:
        # At a high level performs:
        #   sp--
        #   addr = segment + i
        #   *addr = *sp
        return "\n".join(
            [
                # Decrement stack, sp--
                "@SP",
                "M=M-1",
                # calculate addr = segment + i, and storing in a temp register R3
                f"@{self.hack_segment_labels[segment]}",  # Load the value stored in LCL
                "D=M",
                f"@{i}",
                "D=D+A",
                "@R13",
                "M=D",
                # D=*sp
                "@SP",
                "A=M",
                "D=M",
                # *addr = *sp
                "@R13",
                "A=M",
                "M=D",
                # Not Needed, but clean up R13:
                "@R13",
                "M=0",
            ]
        )

    def label(self, label: str) -> str:
        return f"({label})"

    def goto(self, label: str) -> str:
        return "\n".join(
            # fmt: off
            [
                f"@{label}",
                "0;JMP"
            ]
            # fmt: on
        )

    def if_goto(self, label: str) -> str:
        # condition=pop()
        # if condition, don't jump.
        return "\n".join(
            # fmt: off
            [
                "@SP",
                "AM=M-1",
                "D=M",
                f"@{label}",
                "D;JNE"
            ]
            # fmt: on
        )

    def call(self, name: str, local_variable_count: int) -> str:
        # At a high level this performs:
        #   push returnAddress // Using a unique label
        #   push LCL
        #   push ARG
        #   push THIS
        #   push THAT
        #   ARG = SP - 5 - nArgs
        #   LCL = SP
        #   goto functionName // Transfer control to the required function
        #   (returnAddress) // Declare label for the return address

        self.call_count = self.call_count + 1
        return_label = f"{self.namespace}$Ret.{self.call_count}"
        return "\n".join(
            [
                self.push_constant(return_label),
                self.push_segment_value("LCL"),
                self.push_segment_value("ARG"),
                self.push_segment_value("THIS"),
                self.push_segment_value("THAT"),
                # # ARG = SP - 5 - nArgs
                "@SP",
                "D=M",
                "@5",
                "D=D-A",
                f"@{local_variable_count}",
                "D=D-A",
                "@ARG",
                "M=D",
                # LCL=SP
                "@SP",
                "D=M",
                "@LCL",
                "M=D",
                # goto functionName
                f"@{name} // Jump to function {name}",
                "0;JMP",
                # return label for when the function call completes
                f"({return_label})",
            ]
        )

    def function(self, name: str, local_variable_count: int) -> str:
        # Label the current function so that is can be jumped to, and initialize all local variables to zero
        return "\n".join([f"({name})"] + [self.push_constant(0)] * local_variable_count)

    def return_statement(self) -> str:
        # At a high level this performs:
        #   endFrame = LCL
        #   returnAddress = *(endFrame - frame_size)
        #   *arg = pop()
        #   sp = arg + 1
        #   Recover previous frame's state
        #   that = *(endFrame - 1)
        #   this = *(endFrame - 2)
        #   arg = *(endFrame - 3)
        #   lcl = *(endFrame - 4)
        #   goto returnAddress
        restore_frames: List[str] = []
        for frame in ["THAT", "THIS", "ARG", "LCL"]:
            # fmt: on
            restore_frames += ["@R13", "M=M-1", "A=M", "D=M", f"@{frame}", "M=D"]
            # fmt: on

        return "\n".join(
            [
                # R13 = endFrame
                "@LCL",
                "D=M",
                "@R13",
                "MD=D",
                # R14 = *(endFrame - 5)
                "@5",
                "A=D-A",
                "D=M",
                "@R14",
                "M=D",
                # *arg = pop()
                "@SP",
                "A=M-1",
                "D=M",
                "@ARG",
                "A=M",
                "M=D",
                # # sp = arg + 1
                "@ARG",
                "D=M+1",
                "@SP",
                "M=D",
            ]
            + restore_frames
            # goto returnAddress
            + ["@R14", "A=M", "0;JMP"]
        )
