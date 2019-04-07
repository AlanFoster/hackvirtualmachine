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


    # Visit a parse tree produced by VMParser#segment.
    def visitSegment(self, ctx:VMParser.SegmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VMParser#goto.
    def visitGoto(self, ctx:VMParser.GotoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VMParser#ifGoto.
    def visitIfGoto(self, ctx:VMParser.IfGotoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VMParser#label.
    def visitLabel(self, ctx:VMParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VMParser#labelIdentifier.
    def visitLabelIdentifier(self, ctx:VMParser.LabelIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VMParser#call.
    def visitCall(self, ctx:VMParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VMParser#argumentCount.
    def visitArgumentCount(self, ctx:VMParser.ArgumentCountContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VMParser#function.
    def visitFunction(self, ctx:VMParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VMParser#functionName.
    def visitFunctionName(self, ctx:VMParser.FunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VMParser#localVariableCount.
    def visitLocalVariableCount(self, ctx:VMParser.LocalVariableCountContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VMParser#returnStatement.
    def visitReturnStatement(self, ctx:VMParser.ReturnStatementContext):
        return self.visitChildren(ctx)



del VMParser