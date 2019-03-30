import antlr4
from parser.VMLexer import VMLexer
from parser.VMParser import VMParser
from hack.Visitor import Visitor


class VmToHack:
    @staticmethod
    def convert(input_stream):
        lexer = VMLexer(input_stream)
        stream = antlr4.CommonTokenStream(lexer)
        parser = VMParser(stream)
        tree = parser.program()

        visitor = Visitor()
        return visitor.visit(tree)
