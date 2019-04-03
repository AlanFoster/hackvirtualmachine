import antlr4
from parser.VMLexer import VMLexer
from parser.VMParser import VMParser
from hack.Visitor import Visitor
from .Generator import Generator


class VmToHack:
    @staticmethod
    def convert(namespace, input_stream):
        lexer = VMLexer(input_stream)
        stream = antlr4.CommonTokenStream(lexer)
        parser = VMParser(stream)
        tree = parser.program()

        generator = Generator(namespace)
        visitor = Visitor(generator)
        return visitor.visit(tree)
