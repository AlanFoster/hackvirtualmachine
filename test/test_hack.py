import antlr4
from hack.VmToHack import VmToHack


def convert(vm_input):
    return VmToHack.convert(antlr4.InputStream(vm_input))


def combine(instructions):
    return '\n'.join(instructions) + '\n'


def test_push_constant():
    vm_input = "push constant 1337"
    expected = combine([
        "// push constant 1337",
        "@1337",
        "D=A",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
    ])

    assert convert(vm_input) == expected


def test_push_local():
    vm_input = "push local 6"
    expected = combine([
        "// push local 6",
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
        "// push argument 12",
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
        "// push temp 3",
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


def test_add():
    vm_input = "add"
    expected = combine([
        "// add",
        "@SP",
        "M=M-1",
        "@SP",
        "A=M",
        "D=M",
        "@SP",
        "M=M-1",
        "@SP",
        "A=M",
        "D=D+M",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1"
    ])

    assert convert(vm_input) == expected
