import sys
import antlr4
from hack.VmToHack import VmToHack


def main(argv):
    input_stream = antlr4.FileStream(argv[1])
    result = VmToHack.convert(input_stream)
    print(result)

    with open('output.asm', 'w') as file:
        file.write(result)


if __name__ == '__main__':
    main(sys.argv)
