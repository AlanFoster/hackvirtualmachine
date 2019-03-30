# Generated from VM.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .VMParser import VMParser
else:
    from VMParser import VMParser

# This class defines a complete listener for a parse tree produced by VMParser.
class VMListener(ParseTreeListener):

    # Enter a parse tree produced by VMParser#program.
    def enterProgram(self, ctx:VMParser.ProgramContext):
        pass

    # Exit a parse tree produced by VMParser#program.
    def exitProgram(self, ctx:VMParser.ProgramContext):
        pass


    # Enter a parse tree produced by VMParser#statements.
    def enterStatements(self, ctx:VMParser.StatementsContext):
        pass

    # Exit a parse tree produced by VMParser#statements.
    def exitStatements(self, ctx:VMParser.StatementsContext):
        pass


    # Enter a parse tree produced by VMParser#statement.
    def enterStatement(self, ctx:VMParser.StatementContext):
        pass

    # Exit a parse tree produced by VMParser#statement.
    def exitStatement(self, ctx:VMParser.StatementContext):
        pass


    # Enter a parse tree produced by VMParser#push.
    def enterPush(self, ctx:VMParser.PushContext):
        pass

    # Exit a parse tree produced by VMParser#push.
    def exitPush(self, ctx:VMParser.PushContext):
        pass


    # Enter a parse tree produced by VMParser#pop.
    def enterPop(self, ctx:VMParser.PopContext):
        pass

    # Exit a parse tree produced by VMParser#pop.
    def exitPop(self, ctx:VMParser.PopContext):
        pass


    # Enter a parse tree produced by VMParser#arithmetic.
    def enterArithmetic(self, ctx:VMParser.ArithmeticContext):
        pass

    # Exit a parse tree produced by VMParser#arithmetic.
    def exitArithmetic(self, ctx:VMParser.ArithmeticContext):
        pass


    # Enter a parse tree produced by VMParser#logical.
    def enterLogical(self, ctx:VMParser.LogicalContext):
        pass

    # Exit a parse tree produced by VMParser#logical.
    def exitLogical(self, ctx:VMParser.LogicalContext):
        pass


    # Enter a parse tree produced by VMParser#stack.
    def enterStack(self, ctx:VMParser.StackContext):
        pass

    # Exit a parse tree produced by VMParser#stack.
    def exitStack(self, ctx:VMParser.StackContext):
        pass


