import antlr4
from dataclasses import dataclass
from typing import List
from parser.VMLexer import VMLexer
from parser.VMParser import VMParser
from hack.Visitor import Visitor
from .Generator import Generator


@dataclass
class Input:
    namespace: str
    stream: antlr4.InputStream


class VmToHack:
    @staticmethod
    def convert(inputs: List[Input]) -> str:
        result = "" if len(inputs) <= 1 else Generator("bootstrap").bootstrap()

        for input in inputs:
            generator = Generator(input.namespace)
            visitor = Visitor(generator)

            if result is None:
                result = generator.bootstrap()

            lexer = VMLexer(input.stream)
            tokens = antlr4.CommonTokenStream(lexer)
            parser = VMParser(tokens)
            tree = parser.program()

            result = result + visitor.visit(tree)

        return result
