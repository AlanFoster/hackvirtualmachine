def push_operation(operation):
    """
    Pushes the current value assigned to the D register onto the stack
    """

    def wrapper(*args, **kwargs) -> str:
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


def pop_operation(operation):
    def wrapper(*args, **kwargs) -> str:
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


def unary_operation(operation):
    """
    Replaces the top value on the stack with the given computation
    """

    def wrapper(*args, **kwargs) -> str:
        return "\n".join(
            # fmt: off
            [
                "@SP",
                "A=M-1",
            ] + operation(*args, **kwargs)
            # fmt: on
        )

    return wrapper


def binary_operation(operation):
    """
    Pop the top two values from the stack, and push the given binary computation result back onto the stack.
    """

    def wrapper(*args, **kwargs) -> str:
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


def pointer_name(pointer):
    pointer_labels = {"0": "THIS", "1": "THAT"}
    if pointer not in pointer_labels:
        raise ValueError(
            f'Pointer target may only be 0 (THIS) or 1 (THAT), instead received "{pointer}"'
        )
    return pointer_labels[pointer]


def temp_register(i):
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
    }  # fmt: on

    def __init__(self, namespace):
        self.namespace = namespace
        self.comparison_count = 0

    @push_operation
    def visit_push_static(self, i):
        return [
            # Load global address
            f"@{self.namespace}.{i}",
            "D=M",
        ]

    @push_operation
    def visit_push_constant(self, value):
        return [
            # Set constant in stack pointer
            f"@{value}",
            "D=A",
        ]

    @push_operation
    def visit_push_pointer(self, pointer):
        # fmt:off
        return [
            f"@{pointer_name(pointer)}",
            "D=M",
        ]
        # fmt:on

    @push_operation
    def visit_push_segment(self, segment, i):
        return [
            # Calculating addr, where addr = LCL + i
            f"@{self.hack_segment_labels[segment]}",  # Load the value stored in segment
            "D=M",
            f"@{i}",  # Load i
            "A=D+A",  # Set address register to addr
            "D=M",  # Load the value stored within addr, i.e. *addr
        ]

    @push_operation
    def visit_push_temp(self, i):
        return [
            f"@{temp_register(i)}",
            "D=M",
        ]

    @binary_operation
    def visit_comparison_operator(self, operator):
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
    def visit_sub(self):
        return ["M=M-D"]

    @binary_operation
    def visit_add(self):
        return ["M=M+D"]

    @unary_operation
    def visit_neg(self):
        return ["M=-M"]

    @binary_operation
    def visit_and(self):
        return ["M=D&M"]

    @binary_operation
    def visit_or(self):
        return ["M=D|M"]

    @unary_operation
    def visit_not(self):
        return ["M=!M"]

    @pop_operation
    def visit_pop_temp(self, i):
        return [
            # Store the new value
            f"@{temp_register(i)}",
            "M=D",
        ]

    @pop_operation
    def visit_pop_pointer(self, pointer):
        return [
            # Store the new value
            f"@{pointer_name(pointer)}",
            "M=D",
        ]

    @pop_operation
    def visit_pop_static(self, i):
        return [
            # Store the new value
            f"@{self.namespace}.{i}",
            "M=D",
        ]

    def visit_pop_segment(self, segment, i):
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
