import antlr4
from pathlib import Path
from dataclasses import dataclass
from hack.VmToHack import VmToHack, Input
from typing import List, Any
import sys


@dataclass(frozen=True)
class Configuration:
    files: List[Path]
    output: Path


def parse_config(argv: List[Any]) -> Configuration:
    input_path = Path(argv[1]).absolute()

    if input_path.is_file():
        return Configuration(files=[input_path], output=input_path.with_suffix(".asm"))
    else:
        return Configuration(
            files=list(input_path.glob("*.vm")),
            output=input_path.joinpath(input_path.with_suffix(".asm").name),
        )


def main(argv: List[Any]) -> None:
    configuration = parse_config(argv)
    inputs = [
        Input(namespace=file.name, stream=antlr4.FileStream(str(file)))
        for file in configuration.files
    ]

    result = VmToHack.convert(inputs=inputs)
    print(result)
    with configuration.output.open(mode="w") as file:
        file.write(result)


if __name__ == "__main__":
    main(sys.argv)
