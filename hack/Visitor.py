from parser.VMParser import VMParser
from parser.VMVisitor import VMVisitor


class Visitor(VMVisitor):
    # Visit a parse tree produced by VMParser#program.
    def visitProgram(self, ctx: VMParser.ProgramContext):
        return self.visitStatements(ctx.statements())

    # Visit a parse tree produced by VMParser#statements.
    def visitStatements(self, ctx: VMParser.StatementsContext):
        return '\n'.join([self.visit(child) for child in ctx.getChildren()]) + '\n'

    # Visit a parse tree produced by VMParser#statement.
    def visitStatement(self, ctx: VMParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by VMParser#push.
    def visitPush(self, ctx: VMParser.PushContext):
        segment = ctx.segment().getText()

        # Mapping human readable virtual machine names to the hack assembly labels
        hack_segment_names = {
            'local': 'LCL',
            'argument': 'ARG',
            'this': 'THIS',
            'that': 'THAT'
        }

        if segment == 'constant':
            value = ctx.INT().getText()
            return '\n'.join([
                # Set constant in stack pointer
                f"@{value}",
                "D=A",
                "@SP",
                "M=D",

                # Increment stack, sp++
                "@SP",
                "M=M+1",
            ])
        elif segment in hack_segment_names:
            i = ctx.INT().getText()

            return '\n'.join([
                # Calculating addr, where addr = LCL + i
                f"@{hack_segment_names[segment]}",  # Load the value stored in LCL
                "D=M",
                f"@{i}",  # Load i
                "D=D+M",  # D is now addr = LCL + i

                "D=M",  # Load the value stored within addr, i.e. *addr
                "@SP",  # Fetch the segment pointer
                "A=M",  # Load *sp into the address register
                "M=D",  # *sp = *addr

                # Increment stack, sp++
                "@SP",
                "M=M+1"
            ])
        else:
            raise ValueError(f'unexpected segment value: "{segment}"')


# Visit a parse tree produced by VMParser#pop.
def visitPop(self, ctx: VMParser.PopContext):
    return "pop " + self.visit(ctx.segment()) + " " + ctx.INT().getText()

    # Visit a parse tree produced by VMParser#arithmetic.


def visitArithmetic(self, ctx: VMParser.ArithmeticContext):
    return ctx.getText()

    # Visit a parse tree produced by VMParser#logical.


def visitLogical(self, ctx: VMParser.LogicalContext):
    return ctx.getText()
