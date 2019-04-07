from parser.VMParser import VMParser
from parser.VMVisitor import VMVisitor


class Visitor(VMVisitor):
    def __init__(self, generator):
        self.generator = generator

    # Visit a parse tree produced by VMParser#program.
    def visitProgram(self, ctx: VMParser.ProgramContext):
        return self.visitStatements(ctx.statements())

    # Visit a parse tree produced by VMParser#statements.
    def visitStatements(self, ctx: VMParser.StatementsContext):
        preamble = [
            # "// Set SP pointer",
            # "@20",
            # "D=A",
            # "@SP",
            # "M=D",
            # "// Set local pointer",
            # "@25",
            # "D=A",
            # "@LCL",
            # "M=D",
        ]
        instructions = [self.visit(child) for child in ctx.getChildren()]
        return "\n".join(preamble + instructions) + "\n"

    # Visit a parse tree produced by VMParser#statement.
    def visitStatement(self, ctx: VMParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by VMParser#push.
    def visitPush(self, ctx: VMParser.PushContext):
        segment = ctx.segment().getText()
        i = ctx.INT().getText()
        comment = f"// push {segment} {i}\n"

        if segment == "constant":
            return comment + self.generator.visit_push_constant(i)
        elif segment == "static":
            return comment + self.generator.visit_push_static(i)
        elif segment == "pointer":
            return comment + self.generator.visit_push_pointer(i)
        elif segment == "temp":
            return comment + self.generator.visit_push_temp(i)
        elif segment in self.generator.hack_segment_labels:
            return comment + self.generator.visit_push_segment(segment, i)
        else:
            raise ValueError(f'unexpected segment value: "{segment}"')

    # Visit a parse tree produced by VMParser#pop.
    def visitPop(self, ctx: VMParser.PopContext):
        segment = ctx.segment().getText()
        i = ctx.INT().getText()
        comment = f"// pop {segment} {i}\n"

        if segment == "temp":
            return comment + self.generator.visit_pop_temp(i)
        elif segment == "pointer":
            return comment + self.generator.visit_pop_pointer(i)
        elif segment == "static":
            return comment + self.generator.visit_pop_static(i)
        elif segment in self.generator.hack_segment_labels:
            return comment + self.generator.visit_pop_segment(segment, i)
        else:
            raise ValueError(f'unexpected segment value: "{segment}"')

    # Visit a parse tree produced by VMParser#arithmetic.
    def visitArithmetic(self, ctx: VMParser.ArithmeticContext):
        operation = ctx.getText()
        comment = f"// {operation}\n"

        if operation == "add":
            return comment + self.generator.visit_add()
        elif operation == "sub":
            return comment + self.generator.visit_sub()
        elif operation == "neg":
            return comment + self.generator.visit_neg()
        else:
            raise ValueError(f'unexpected arithmetic value: "{operation}"')

    # Visit a parse tree produced by VMParser#logical.
    def visitLogical(self, ctx: VMParser.LogicalContext):
        operator = ctx.getText()
        comment = f"// {operator}\n"

        if operator == "not":
            return comment + self.generator.visit_not()
        elif operator in self.generator.comparison_operators:
            return comment + self.generator.visit_comparison_operator(operator)
        elif operator == "and":
            return comment + self.generator.visit_and()
        elif operator == "or":
            return comment + self.generator.visit_or()
        else:
            raise ValueError(f'Unexpected logical operation "{operator}"')

    # Visit a parse tree produced by VMParser#label.
    def visitLabel(self, ctx: VMParser.LabelContext):
        label = ctx.LABEL_IDENTIFIER().getText()
        raise ValueError(f"label {label} not supported yet.")

    # Visit a parse tree produced by VMParser#goto.
    def visitGoto(self, ctx: VMParser.GotoContext):
        label = ctx.LABEL_IDENTIFIER().getText()
        raise ValueError(f"goto {label} not supported yet.")

    # Visit a parse tree produced by VMParser#ifGoto.
    def visitIfGoto(self, ctx: VMParser.IfGotoContext):
        label = ctx.LABEL_IDENTIFIER().getText()
        raise ValueError(f"if-goto {label} not supported yet.")
