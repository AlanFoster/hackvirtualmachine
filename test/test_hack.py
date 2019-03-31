import antlr4
from hack.VmToHack import VmToHack


def convert(vm_input):
    return VmToHack.convert(antlr4.InputStream(vm_input))


def combine(instructions):
    return '\n'.join(instructions) + '\n'


def test_push_constant():
    vm_input = "push constant 1337"
    expected = combine([
        "@1337",
        "D=A",
        "@SP",
        "M=D",
        "@SP",
        "M=M+1",
    ])

    assert convert(vm_input) == expected


def test_push_local():
    vm_input = "push local 6"
    expected = combine([
        "@LCL",
        "D=M",
        "@6",
        "D=D+M",
        "D=M",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
    ])

    assert convert(vm_input) == expected


def test_push_argument():
    vm_input = "push argument 12"
    expected = combine([
        "@ARG",
        "D=M",
        "@12",
        "D=D+M",
        "D=M",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
    ])

    assert convert(vm_input) == expected


def test_push_temp():
    vm_input = "push temp 3"
    expected = combine([
        "@8",
        "D=A",
        "D=M",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
    ])

    assert convert(vm_input) == expected
