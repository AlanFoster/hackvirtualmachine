from typing import cast
from parser.VMParser import VMParser
from parser.VMVisitor import VMVisitor
from .Generator import Generator


class Visitor(VMVisitor):
    def __init__(self, generator: Generator):
        self.generator = generator

    # Visit a parse tree produced by VMParser#program.
    def visitProgram(self, ctx: VMParser.ProgramContext) -> str:
        return self.visitStatements(ctx.statements())

    # Visit a parse tree produced by VMParser#statements.
    def visitStatements(self, ctx: VMParser.StatementsContext) -> str:
        instructions = [self.visit(child) for child in ctx.getChildren()]
        return "\n".join(instructions) + "\n"

    # Visit a parse tree produced by VMParser#statement.
    def visitStatement(self, ctx: VMParser.StatementContext) -> str:
        return cast(str, self.visitChildren(ctx))

    # Visit a parse tree produced by VMParser#push.
    def visitPush(self, ctx: VMParser.PushContext) -> str:
        segment = ctx.segment().getText()
        i = ctx.INT().getText()
        comment = f"// push {segment} {i}\n"

        if segment == "constant":
            return comment + self.generator.push_constant(i)
        elif segment == "static":
            return comment + self.generator.push_static(i)
        elif segment == "pointer":
            return comment + self.generator.push_pointer(i)
        elif segment == "temp":
            return comment + self.generator.push_temp(i)
        elif segment in self.generator.hack_segment_labels:
            return comment + self.generator.push_segment(segment, i)
        else:
            raise ValueError(f'unexpected segment value: "{segment}"')

    # Visit a parse tree produced by VMParser#pop.
    def visitPop(self, ctx: VMParser.PopContext) -> str:
        segment = ctx.segment().getText()
        i = ctx.INT().getText()
        comment = f"// pop {segment} {i}\n"

        if segment == "temp":
            return comment + self.generator.pop_temp(i)
        elif segment == "pointer":
            return comment + self.generator.pop_pointer(i)
        elif segment == "static":
            return comment + self.generator.pop_static(i)
        elif segment in self.generator.hack_segment_labels:
            return comment + self.generator.pop_segment(segment, i)
        else:
            raise ValueError(f'unexpected segment value: "{segment}"')

    # Visit a parse tree produced by VMParser#arithmetic.
    def visitArithmetic(self, ctx: VMParser.ArithmeticContext) -> str:
        operation = ctx.getText()
        comment = f"// {operation}\n"

        if operation == "add":
            return comment + self.generator.add()
        elif operation == "sub":
            return comment + self.generator.sub()
        elif operation == "neg":
            return comment + self.generator.neg()
        else:
            raise ValueError(f'unexpected arithmetic value: "{operation}"')

    # Visit a parse tree produced by VMParser#logical.
    def visitLogical(self, ctx: VMParser.LogicalContext) -> str:
        operator = ctx.getText()
        comment = f"// {operator}\n"

        if operator == "not":
            return comment + self.generator.logical_not()
        elif operator in self.generator.comparison_operators:
            return comment + self.generator.comparison_operator(operator)
        elif operator == "and":
            return comment + self.generator.logical_and()
        elif operator == "or":
            return comment + self.generator.logical_or()
        else:
            raise ValueError(f'Unexpected logical operation "{operator}"')

    # Visit a parse tree produced by VMParser#label.
    def visitLabel(self, ctx: VMParser.LabelContext) -> str:
        label = ctx.labelIdentifier().getText()
        comment = f"// label {label}\n"

        return comment + self.generator.label(label)

    # Visit a parse tree produced by VMParser#goto.
    def visitGoto(self, ctx: VMParser.GotoContext) -> str:
        label = ctx.labelIdentifier().getText()
        comment = f"// goto {label}\n"

        return comment + self.generator.goto(label)

    # Visit a parse tree produced by VMParser#ifGoto.
    def visitIfGoto(self, ctx: VMParser.IfGotoContext) -> str:
        label = ctx.labelIdentifier().getText()
        comment = f"// if-goto {label}\n"

        return comment + self.generator.if_goto(label)

    # Visit a parse tree produced by VMParser#call.
    def visitCall(self, ctx: VMParser.CallContext) -> str:
        name = ctx.functionName().getText()
        argument_count = int(ctx.argumentCount().getText())
        comment = f"// call {name} {argument_count}\n"

        return comment + self.generator.call(name, argument_count)

    # Visit a parse tree produced by VMParser#function.
    def visitFunction(self, ctx: VMParser.FunctionContext) -> str:
        name = ctx.functionName().getText()
        local_variable_count = int(ctx.localVariableCount().getText())
        comment = f"// function {name} {local_variable_count}\n"

        return comment + self.generator.function(name, local_variable_count)

    # Visit a parse tree produced by VMParser#returnStatement.
    def visitReturnStatement(self, ctx: VMParser.ReturnStatementContext) -> str:
        comment = "// return\n"

        return comment + self.generator.return_statement()
