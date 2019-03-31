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
        "D=D+A",
        "A=D",
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
        "D=D+A",
        "A=D",
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
        "A=D",
        "D=M",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
    ])

    assert convert(vm_input) == expected


def test_push_static():
    vm_input = "push static 3"
    expected = combine([
        "// push static 3",
        "@GeneratedGlobalConstant.3",
        "D=M",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1",
    ])

    assert convert(vm_input) == expected


def test_pop_temp():
    vm_input = "pop temp 3"
    expected = combine([
        "// pop temp 3",
        "@SP",
        "M=M-1",
        "@SP",
        "A=M",
        "D=M",
        "@8",
        "M=D",
    ])

    assert convert(vm_input) == expected


def test_pop_local():
    vm_input = "pop local 3"
    expected = combine([
        "// pop local 3",
        "@SP",
        "M=M-1",
        "@LCL",
        "D=M",
        "@3",
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
    ])

    assert convert(vm_input) == expected


def test_pop_static():
    vm_input = "pop static 3"
    expected = combine([
        "// pop static 3",
        "@SP",
        "M=M-1",
        "@SP",
        "A=M",
        "D=M",
        "@GeneratedGlobalConstant.3",
        "M=D",
    ])

    print(convert(vm_input))

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
        "D=M+D",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1"
    ])

    assert convert(vm_input) == expected


def test_sub():
    vm_input = "sub"
    expected = combine([
        "// sub",
        "@SP",
        "M=M-1",
        "@SP",
        "A=M",
        "D=M",
        "@SP",
        "M=M-1",
        "@SP",
        "A=M",
        "D=M-D",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1"
    ])

    assert convert(vm_input) == expected
