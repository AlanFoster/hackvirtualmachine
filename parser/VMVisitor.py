# Generated from VM.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .VMParser import VMParser
else:
    from VMParser import VMParser

# This class defines a complete generic visitor for a parse tree produced by VMParser.

class VMVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VMParser#program.
    def visitProgram(self, ctx:VMParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VMParser#statements.
    def visitStatements(self, ctx:VMParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VMParser#statement.
    def visitStatement(self, ctx:VMParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VMParser#push.
    def visitPush(self, ctx:VMParser.PushContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VMParser#pop.
    def visitPop(self, ctx:VMParser.PopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VMParser#arithmetic.
    def visitArithmetic(self, ctx:VMParser.ArithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VMParser#logical.
    def visitLogical(self, ctx:VMParser.LogicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VMParser#stack.
    def visitStack(self, ctx:VMParser.StackContext):
        return self.visitChildren(ctx)



del VMParser