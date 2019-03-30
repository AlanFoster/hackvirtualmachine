import antlr4
from hack.VmToHack import VmToHack


def convert(vm_input):
    return VmToHack.convert(antlr4.InputStream(vm_input))


def test_push_constant():
    vm_input = \
        "push constant 10\n" \
        "pop local 0\n" \
        "push constant 21\n" \
        "push constant 22\n" \
        "pop argument 2\n" \
        "pop argument 1\n" \
        "push constant 36\n" \
        "pop this 6\n" \
        "push constant 42\n" \
        "push constant 45\n" \
        "pop that 5\n" \
        "pop that 2\n" \
        "push constant 510\n" \
        "pop temp 6\n" \
        "push local 0\n" \
        "push that 5\n" \
        "add\n" \
        "push argument 1\n" \
        "sub\n" \
        "push this 6\n" \
        "push this 6\n" \
        "add\n" \
        "sub\n" \
        "push temp 6\n" \
        "add"
    assert convert(vm_input) == vm_input
