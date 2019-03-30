from parser.VMParser import VMParser
from parser.VMVisitor import VMVisitor


class Visitor(VMVisitor):
    # Visit a parse tree produced by VMParser#program.
    def visitProgram(self, ctx: VMParser.ProgramContext):
        return self.visitStatements(ctx.statements())

    # Visit a parse tree produced by VMParser#statements.
    def visitStatements(self, ctx: VMParser.StatementsContext):
        return '\n'.join([self.visit(child) for child in ctx.getChildren()])

    # Visit a parse tree produced by VMParser#statement.
    def visitStatement(self, ctx: VMParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by VMParser#push.
    def visitPush(self, ctx: VMParser.PushContext):
        return "push " + self.visit(ctx.stack()) + " " + ctx.INT().getText()

    # Visit a parse tree produced by VMParser#pop.
    def visitPop(self, ctx: VMParser.PopContext):
        return "pop " + self.visit(ctx.stack()) + " " + ctx.INT().getText()

    # Visit a parse tree produced by VMParser#arithmetic.
    def visitArithmetic(self, ctx: VMParser.ArithmeticContext):
        return ctx.getText()

    # Visit a parse tree produced by VMParser#logical.
    def visitLogical(self, ctx: VMParser.LogicalContext):
        return ctx.getText()

    # Visit a parse tree produced by VMParser#stack.
    def visitStack(self, ctx: VMParser.StackContext):
        return ctx.getText()
