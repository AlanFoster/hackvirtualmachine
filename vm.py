import sys
import antlr4
from pathlib import Path
from dataclasses import dataclass
from hack.VmToHack import VmToHack


@dataclass(frozen=True)
class Configuration:
    files: [str]
    output: str


def parse_config(argv) -> Configuration:
    input_path = Path(argv[1]).absolute()

    if input_path.is_file():
        return Configuration(files=[input_path], output=input_path.with_suffix(".asm"))
    else:
        return Configuration(
            files=list(input_path.glob("*.vm")),
            output=input_path.joinpath(input_path.with_suffix(".asm").name),
        )


def main(argv):
    configuration = parse_config(argv)
    inputs = [[file.name, antlr4.FileStream(file)] for file in configuration.files]

    result = VmToHack.convert(inputs=inputs)
    print(result)

    with open(configuration.output, "w") as file:
        file.write(result)


if __name__ == "__main__":
    main(sys.argv)
