import antlr4
from parser.VMLexer import VMLexer
from parser.VMParser import VMParser
from hack.Visitor import Visitor
from .Generator import Generator


class VmToHack:
    @staticmethod
    def convert(inputs):
        result = "" if len(inputs) <= 1 else Generator(None).bootstrap()

        for namespace, stream in inputs:
            generator = Generator(namespace)
            visitor = Visitor(generator)

            if result is None:
                result = generator.bootstrap()

            lexer = VMLexer(stream)
            tokens = antlr4.CommonTokenStream(lexer)
            parser = VMParser(tokens)
            tree = parser.program()

            result = result + visitor.visit(tree)

        return result
