from parser.VMParser import VMParser
from parser.VMVisitor import VMVisitor


class Visitor(VMVisitor):
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
            # "M=A",
        ]
        instructions = [self.visit(child) for child in ctx.getChildren()]
        return "\n".join(preamble + instructions) + "\n"

    # Visit a parse tree produced by VMParser#statement.
    def visitStatement(self, ctx: VMParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by VMParser#push.
    def visitPush(self, ctx: VMParser.PushContext):
        segment = ctx.segment().getText()

        # Mapping human readable virtual machine names to the hack assembly labels
        hack_segment_names = {
            "local": "LCL",
            "argument": "ARG",
            "this": "THIS",
            "that": "THAT",
        }

        if segment == "constant":
            value = ctx.INT().getText()
            return "\n".join(
                [
                    f"// push constant {value}",
                    # Set constant in stack pointer
                    f"@{value}",
                    "D=A",
                    "@SP",
                    "A=M",
                    "M=D",
                    # Increment stack, sp++
                    "@SP",
                    "M=M+1",
                ]
            )
        elif segment == "static":
            i = int(ctx.INT().getText())
            global_name = (
                "GeneratedGlobalConstant"
            )  # TODO: This should be extracted from the file name

            return "\n".join(
                [
                    f"// push static {i}",
                    # Load global address
                    f"@{global_name}.{i}",
                    "D=M",
                    # *sp = *addr
                    "@SP",  # Fetch the segment pointer
                    "A=M",  # Load *sp into the address register
                    "M=D",  # *sp = *addr
                    # Increment stack, sp++
                    "@SP",
                    "M=M+1",
                ]
            )
        elif segment == "temp":
            i = int(ctx.INT().getText())

            temp_registers_start = 5
            temp_registers_end = 12
            allocated_register = temp_registers_start + i

            if allocated_register > temp_registers_end:
                raise ValueError(
                    f'Unexpected temp register value: "{allocated_register}". This would cause overflow;.'
                    f"Available registers: R{temp_registers_start}-R{temp_registers_end}"
                )

            return "\n".join(
                [
                    f"// push temp {i}",
                    # Calculating addr, where addr = LCL + i
                    f"@{allocated_register}",  # Load the value stored in LCL
                    "D=A",  # D is now addr = temp_registers_start + i
                    "A=D",  # Set address register to addr
                    "D=M",  # Load the value stored within addr, i.e. *addr
                    # *sp = *addr
                    "@SP",  # Fetch the segment pointer
                    "A=M",  # Load *sp into the address register
                    "M=D",  # *sp = *addr
                    # Increment stack, sp++
                    "@SP",
                    "M=M+1",
                ]
            )
        elif segment in hack_segment_names:
            i = ctx.INT().getText()

            # At a high level performs:
            #   addr = segment + i
            #   *sp = *addr
            #   sp++
            return "\n".join(
                [
                    f"// push {segment} {i}",
                    # Calculating addr, where addr = LCL + i
                    f"@{hack_segment_names[segment]}",  # Load the value stored in LCL
                    "D=M",
                    f"@{i}",  # Load i
                    "D=D+A",  # D is now addr = LCL + i
                    "A=D",  # Set address register to addr
                    "D=M",  # Load the value stored within addr, i.e. *addr
                    # *sp = *addr
                    "@SP",  # Fetch the segment pointer
                    "A=M",  # Load *sp into the address register
                    "M=D",  # *sp = *addr
                    # Increment stack, sp++
                    "@SP",
                    "M=M+1",
                ]
            )
        else:
            raise ValueError(f'unexpected segment value: "{segment}"')

    # Visit a parse tree produced by VMParser#pop.
    def visitPop(self, ctx: VMParser.PopContext):
        segment = ctx.segment().getText()

        # Mapping human readable virtual machine names to the hack assembly labels
        hack_segment_names = {
            "local": "LCL",
            "argument": "ARG",
            "this": "THIS",
            "that": "THAT",
        }

        if segment == "temp":
            i = int(ctx.INT().getText())

            temp_registers_start = 5
            temp_registers_end = 12
            allocated_register = temp_registers_start + i

            if allocated_register < temp_registers_start:
                raise ValueError(
                    f'Unexpected temp register value: "{allocated_register}". This would cause underflow;.'
                    f"Available registers: R{temp_registers_start}-R{temp_registers_end}"
                )

            return "\n".join(
                [
                    f"// pop temp {i}",
                    # Decrement stack, sp--
                    "@SP",
                    "M=M-1",
                    # Fetch *SP
                    "@SP",
                    "A=M",
                    "D=M",
                    # Store the new value
                    f"@{allocated_register}",
                    "M=D",
                ]
            )
        elif segment == "static":
            i = int(ctx.INT().getText())
            global_name = (
                "GeneratedGlobalConstant"
            )  # TODO: This should be extracted from the file name

            return "\n".join(
                [
                    f"// pop static {i}",
                    # Decrement stack, sp--
                    "@SP",
                    "M=M-1",
                    # Fetch *SP
                    "@SP",
                    "A=M",
                    "D=M",
                    # Store the new value
                    f"@{global_name}.{i}",
                    "M=D",
                ]
            )
        elif segment in hack_segment_names:
            i = ctx.INT().getText()

            # At a high level performs:
            #   sp--
            #   addr = segment + i
            #   *addr = *sp
            return "\n".join(
                [
                    f"// pop {segment} {i}",
                    # Decrement stack, sp--
                    "@SP",
                    "M=M-1",
                    # calculate addr = segment + i, and storing in a temp register R3
                    f"@{hack_segment_names[segment]}",  # Load the value stored in LCL
                    "D=M",
                    f"@{i}",
                    "D=D+A",
                    "@R13",
                    "M=D",
                    # D=*sp
                    "@SP",
                    "A=M",
                    "D=M",
                    # *addr = *sp
                    "@R13",
                    "A=M",
                    "M=D",
                    # Not Needed, but clean up R13:
                    "@R13",
                    "M=0",
                ]
            )
        else:
            raise ValueError(f'unexpected segment value: "{segment}"')

    # Visit a parse tree produced by VMParser#arithmetic.
    def visitArithmetic(self, ctx: VMParser.ArithmeticContext):
        operation = ctx.getText()
        if operation == "add" or operation == "sub":
            return "\n".join(
                [
                    f"// {operation}",
                    # Decrement SP to point to the first value
                    "@SP",
                    "M=M-1",
                    # Store the "top" value of *SP into the D register
                    "@SP",
                    "A=M",
                    "D=M",
                    # Decrement SP to point to the second value
                    "@SP",
                    "M=M-1",
                    # Load the second value of *SP for the required arithmetic operation
                    "@SP",
                    "A=M",
                    # Perform the required arithmetic operation and store the result in D
                    "D=M+D" if operation == "add" else "D=M-D",
                    # Assign the result of the arithmetic operation to *SP
                    "@SP",
                    "A=M",
                    "M=D",
                    # Increment stack, sp++
                    "@SP",
                    "M=M+1",
                ]
            )
        else:
            raise ValueError(f'unexpected arithmetic value: "{operation}"')

    # Visit a parse tree produced by VMParser#logical.
    def visitLogical(self, ctx: VMParser.LogicalContext):
        return ctx.getText()
