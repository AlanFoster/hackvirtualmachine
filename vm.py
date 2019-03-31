import sys
from pathlib import Path
import antlr4
from hack.VmToHack import VmToHack


def main(argv):
    input_path = Path(argv[1]).absolute()
    output_path = Path(input_path).with_suffix(".asm")

    input_stream = antlr4.FileStream(input_path)
    result = VmToHack.convert(input_stream)
    print(result)

    with open(output_path, "w") as file:
        file.write(result)


if __name__ == "__main__":
    main(sys.argv)
