# Hack Virtual Machine Translator

A virtual machine translator for the hack assembly language written with [Antlr](https://www.antlr.org/) and
Python.

## What is it?

Following the through the book `The Elements of Computing Systems`, this project is part of a larger suite of tools:

       +------------+     +-------------+     +------------+
       |    Jack    |     |   Virtual   |     |            |
       |  Compiler  +---->+   Machine   +---->+  Assembler |
       |            |     |  Translator |     |            |
       +------------+     +-------------+     +------------+

### Jack Compiler

The [Jack Compiler](https://github.com/AlanFoster/jackcompiler) converts the high level Jack language into an
intermediate representation which can be ran on a platform agnostic virtual machine. The syntax of Jack is similar to
Java. The virtual machine instructions output by this compiler are stack based, and is modeled after the Java Virtual
Machine (JVM).

This project is written with [ANTLR](https://www.antlr.org/) and Python.

### Hack Virtual Machine Translator

The Jack Compiler outputs virtual machine code. These virtual machine instructions can be compiled using the
[hack virtual machine translator](https://github.com/AlanFoster/hackvirtualmachine). At a high level this tool converts
virtual machine instructions into symbolic assembly commands which can then be passed to an assembler.

This project is written with [ANTLR](https://www.antlr.org/) and Python.

### Hack Assembler

The [Hack Assembler](https://github.com/AlanFoster/hackassembler) takes the symbolic representation of assembly
commands, and converts these instructions into its binary representation using the Hack Assembler. This can then be
loaded on to the Hack platform's ROM and executed.

This project is written with Go.

## Project links

This project is part of a larger suite of tools:

- [Jack Compiler](https://github.com/AlanFoster/jackcompiler) converts the high level Jack language into an
  intermediate representation which can be ran on a platform agnostic virtual machine. Written with [Antlr](https://www.antlr.org/)
  and Python.
- [Hack Virtual Machine Translator](https://github.com/AlanFoster/hackvirtualmachine) - A virtual machine translator
  for the hack assembly language written with [Antlr](https://www.antlr.org/) and Python.
- [Hack Assembler](https://github.com/AlanFoster/hackassembler) - A basic assembler for the Hack symbolic assembly
  language written in Go.

## Supported functionality

Example virtual machine input code:

```assembly
; Computes the sum 1 + 2 + ... + argument[0] and pushes the
; result onto the stack.
push constant 0
pop local 0         ; initializes sum = 0
label LOOP_START
push argument 0
push local 0
add
pop local 0	        ; sum = sum + counter
push argument 0
push constant 1
sub
pop argument 0      ; counter--
push argument 0
if-goto LOOP_START  ; If counter > 0, goto LOOP_START
push local 0
```

This will output symbolic Hack Assembly code, as documented by
[Hack Assembler](https://github.com/AlanFoster/hackassembler). This output can be converted into its binary
representation using the Hack Assembler.

The complete grammar is documented within [VM.g4](./VM.g4)

### Function calls

A caller calls a callee.

- `call function argumentCount` - Prepares for a function call by storing the required return address, and the current
    function's state on the stack - known as its `frame`.
- `function name localVariableCount` - Define a new function with the required number of local variables. This can be jumped
    to using the `call function argumentCount` syntax.
- `return` Return the last value on the current stack and jump back to the previous caller.

### Control Flow

- `label LABEL` - Label the current location so that it can be jumped to. For instance you would use this to mark the
  start of loops.
- `goto LABEL` - Unconditionally jump to the required label.
- `if-goto LABEL` - The stack's topmost value is popped, and if the value is non-zero execution will continue from the
  given label.

### Memory Access

- `pop segment i` - Pop the topmost value from the stack on to the given segment
- `push segment i` - Push the value from the given segment onto the stack

Where segment is one of:

- `local` - Local Variables
- `argument` - Arguments
- `constant` - Only valid when pushing to the stack, i.e. `push constant 10`
- `static` - For global static variables
- `this`
- `that`
- `pointer`
- `temp` - Assign a temporary variable, the Hack hardware provides limited registers to use for this.

### Arithmetic / Logical commands

#### Binary Operations

The following operations the two topmost values within the stack, and pushes the resulting value back onto the stack:

- `add` - Arithmetic addition
- `sub` - Arithmetic subtraction
- `eq`- Logical equality
- `gt`- Logical Greater than
- `lt` - Logical Less Than
- `and` - Logical And
- `or` - Logical Or

#### Unary Operations

The following unary operations pop the topmost value within the stack, and pushes the resulting value back onto the
stack:

- `neg` - Arithmetic negation
- `not` - Logical not

## Notes

### Generate parser

```bash
docker-compose build
docker-compose run --rm service /bin/sh /usr/local/bin/antlr4 VM.g4 -Dlanguage=Python3 -visitor -o parser
```

Unfortunately the generated method names are camel case, rather than snake case - as shown within the python3
codegen templates [here](https://github.com/antlr/antlr4/blob/837aa60e2c4736e242432c2ac93ed2de3b9eff3b/tool/resources/org/antlr/v4/tool/templates/codegen/Python3/Python3.stg#L104)

### Run tests

```bash
docker-compose build
docker-compose run --rm test
```
