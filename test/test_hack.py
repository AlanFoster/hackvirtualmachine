from typing import List

import antlr4
import pytest
from hack.VmToHack import VmToHack, Input


def convert(vm_input: str) -> str:
    return VmToHack.convert(
        [Input(namespace="mock_global_namespace", stream=antlr4.InputStream(vm_input))]
    )


def combine(instructions: List[str]) -> str:
    return "\n".join(instructions) + "\n"


def test_push_constant() -> None:
    vm_input = "push constant 1337"
    expected = combine(
        # fmt: off
        [
            "// push constant 1337",
            "@1337",
            "D=A",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]
        # fmt: on
    )

    assert convert(vm_input) == expected


@pytest.mark.parametrize(
    "segment,index,hack_segment",
    [
        ("local", 10, "LCL"),
        ("argument", 20, "ARG"),
        ("this", 30, "THIS"),
        ("that", 40, "THAT"),
    ],
)
def test_push_segment(segment: str, index: int, hack_segment: str) -> None:
    vm_input = f"push {segment} {index}"
    expected = combine(
        [
            f"// push {segment} {index}",
            f"@{hack_segment}",
            "D=M",
            f"@{index}",
            "A=D+A",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1",
        ]
    )

    assert convert(vm_input) == expected


def test_push_temp() -> None:
    vm_input = "push temp 3"
    expected = combine(
        # fmt: off
        [
            "// push temp 3",
            "@8",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1",
        ]
        # fmt: on
    )

    assert convert(vm_input) == expected


def test_invalid_push_temp() -> None:
    with pytest.raises(ValueError) as e:
        convert("push temp 100")
    assert (
        str(e.value)
        == 'Unexpected temp register value: "105". This would cause overflow. Available registers: R5-R12'
    )


def test_push_static() -> None:
    vm_input = "push static 3"
    expected = combine(
        [
            "// push static 3",
            "@mock_global_namespace.3",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1",
        ]
    )

    assert convert(vm_input) == expected


@pytest.mark.parametrize("target,hack_name", [("0", "THIS"), ("1", "THAT")])
def test_valid_push_pointer(target: str, hack_name: str) -> None:
    vm_input = f"push pointer {target}"
    expected = combine(
        # fmt: off
        [
            f"// push pointer {target}",
            f"@{hack_name}",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1",
        ]
        # fmt: on
    )

    assert convert(vm_input) == expected


def test_invalid_push_pointer() -> None:
    with pytest.raises(ValueError) as e:
        convert("push pointer 100")
    assert (
        str(e.value)
        == 'Pointer target may only be 0 (THIS) or 1 (THAT), instead received "100"'
    )


def test_pop_temp() -> None:
    vm_input = "pop temp 3"
    expected = combine(
        # fmt: off
        [
            "// pop temp 3",
            "@SP",
            "AM=M-1",
            "D=M",
            "@8",
            "M=D",
        ]
        # fmt: on
    )

    assert convert(vm_input) == expected


def test_invalid_pop_temp() -> None:
    with pytest.raises(ValueError) as e:
        convert("pop temp 100")
    assert (
        str(e.value)
        == 'Unexpected temp register value: "105". This would cause overflow. Available registers: R5-R12'
    )


@pytest.mark.parametrize(
    "segment,index,hack_segment",
    [
        ("local", 10, "LCL"),
        ("argument", 20, "ARG"),
        ("this", 30, "THIS"),
        ("that", 40, "THAT"),
    ],
)
def test_pop_segment(segment: str, index: int, hack_segment: str) -> None:
    vm_input = f"pop {segment} {index}"
    expected = combine(
        [
            f"// pop {segment} {index}",
            "@SP",
            "M=M-1",
            f"@{hack_segment}",
            "D=M",
            f"@{index}",
            "D=D+A",
            "@R13",
            "M=D",
            "@SP",
            "A=M",
            "D=M",
            "@R13",
            "A=M",
            "M=D",
            "@R13",
            "M=0",
        ]
    )

    assert convert(vm_input) == expected


def test_pop_static() -> None:
    vm_input = "pop static 3"
    expected = combine(
        # fmt: off
        [
            "// pop static 3",
            "@SP",
            "AM=M-1",
            "D=M",
            "@mock_global_namespace.3",
            "M=D",
        ]
        # fmt: on
    )

    assert convert(vm_input) == expected


@pytest.mark.parametrize("target,hack_name", [("0", "THIS"), ("1", "THAT")])
def test_valid_pop_pointer(target: str, hack_name: str) -> None:
    vm_input = f"pop pointer {target}"
    expected = combine(
        # fmt: off
        [
            f"// pop pointer {target}",
            "@SP",
            "AM=M-1",
            "D=M",
            f"@{hack_name}",
            "M=D",
        ]
        # fmt: on
    )

    assert convert(vm_input) == expected


def test_invalid_pop_pointer() -> None:
    with pytest.raises(ValueError) as e:
        convert("pop pointer 200")
    assert (
        str(e.value)
        == 'Pointer target may only be 0 (THIS) or 1 (THAT), instead received "200"'
    )


@pytest.mark.parametrize("operator,expected", [("add", "M=M+D"), ("sub", "M=M-D")])
def test_math(operator: str, expected: str) -> None:
    vm_input = operator
    expected = combine(
        # fmt: off
        [
            f"// {operator}",
            "@SP",
            "AM=M-1",
            "D=M",
            "A=A-1",
            expected,
        ]
        # fmt: on
    )

    assert convert(vm_input) == expected


def test_neg() -> None:
    vm_input = "neg"
    expected = combine(
        # fmt: off
        [
            "// neg",
            "@SP",
            "A=M-1",
            "M=-M"
        ]
        # fmt: on
    )

    assert convert(vm_input) == expected


def test_not() -> None:
    vm_input = "not"
    expected = combine(
        # fmt: off
        [
            "// not",
            "@SP",
            "A=M-1",
            "M=!M"
        ]
        # fmt: on
    )

    assert convert(vm_input) == expected


@pytest.mark.parametrize(
    "operator,expected", [("eq", "JEQ"), ("gt", "JGT"), ("lt", "JLT")]
)
def test_comparison_operators(operator: str, expected: str) -> None:
    vm_input = operator
    expected = combine(
        # fmt: off
        [
            f"// {operator}",
            "@SP",
            "AM=M-1",
            "D=M",
            "A=A-1",
            "D=M-D",
            f"@{expected}.True.1",
            f"D;{expected}",
            f"({expected}.False.1)",
            "D=0",
            f"@{expected}.Finally.1",
            "0;JMP",
            f"({expected}.True.1)",
            "D=-1",
            f"({expected}.Finally.1)",
            "@SP",
            "A=M-1",
            "M=D",
        ]
        # fmt: on
    )

    assert convert(vm_input) == expected


@pytest.mark.parametrize("operator,expected", [("and", "M=D&M"), ("or", "M=D|M")])
def test_logical_operators(operator: str, expected: str) -> None:
    vm_input = operator
    expected = combine(
        # fmt: off
        [
            f"// {operator}",
            "@SP",
            "AM=M-1",
            "D=M",
            "A=A-1",
            expected,
        ]
        # fmt: on
    )

    assert convert(vm_input) == expected


def test_label() -> None:
    vm_input = "label LOOP_START"
    expected = combine(
        # fmt: off
        [
            "// label LOOP_START",
            "(LOOP_START)"
        ]
        # fmt: on
    )

    assert convert(vm_input) == expected


def test_goto() -> None:
    vm_input = "goto LOOP_START"
    expected = combine(
        # fmt: off
        [
            "// goto LOOP_START",
            "@LOOP_START",
            "0;JMP"
        ]
        # fmt: on
    )

    assert convert(vm_input) == expected


def test_if_goto() -> None:
    vm_input = "if-goto LOOP_START"
    expected = combine(
        # fmt: off
        [
            "// if-goto LOOP_START",
            "@SP",
            "AM=M-1",
            "D=M",
            "@LOOP_START",
            "D;JNE",
        ]
        # fmt: on
    )

    assert convert(vm_input) == expected


def test_call() -> None:
    vm_input = "call function_name 4"
    expected = combine(
        # fmt: off
        [
            "// call function_name 4",
            "@mock_global_namespace$Ret.1",
            "D=A",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1",
            "@LCL",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1",
            "@ARG",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1",
            "@THIS",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1",
            "@THAT",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1",
            "@SP",
            "D=M",
            "@5",
            "D=D-A",
            "@4",
            "D=D-A",
            "@ARG",
            "M=D",
            "@SP",
            "D=M",
            "@LCL",
            "M=D",
            "@function_name // Jump to function function_name",
            "0;JMP",
            "(mock_global_namespace$Ret.1)",
        ]
        # fmt: on
    )

    assert convert(vm_input) == expected


def test_function() -> None:
    vm_input = "function function_name 2"
    expected = combine(
        # fmt: off
        [
            "// function function_name 2",
            "(function_name)",
            # First local variable - `push constant 0`
            "@0",
            "D=A",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1",
            # Second local variable - `push constant 0`
            "@0",
            "D=A",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1",
        ]
        # fmt: on
    )

    assert convert(vm_input) == expected


def test_return() -> None:
    vm_input = "return"
    expected = combine(
        # fmt: off
        [
            "// return",
            "@LCL",
            "D=M",
            "@R13",
            "MD=D",
            "@5",
            "A=D-A",
            "D=M",
            "@R14",
            "M=D",
            "@SP",
            "A=M-1",
            "D=M",
            "@ARG",
            "A=M",
            "M=D",
            "@ARG",
            "D=M+1",
            "@SP",
            "M=D",
            "@R13",
            "M=M-1",
            "A=M",
            "D=M",
            "@THAT",
            "M=D",
            "@R13",
            "M=M-1",
            "A=M",
            "D=M",
            "@THIS",
            "M=D",
            "@R13",
            "M=M-1",
            "A=M",
            "D=M",
            "@ARG",
            "M=D",
            "@R13",
            "M=M-1",
            "A=M",
            "D=M",
            "@LCL",
            "M=D",
            "@R14",
            "A=M",
            "0;JMP",
        ]
        # fmt: on
    )

    assert convert(vm_input) == expected
