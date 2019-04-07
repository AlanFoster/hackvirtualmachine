# Hack Virtual Machine Translator

A virtual machine translator for the hack assembly language written with [Antlr](https://www.antlr.org/) and
Python.

## What is it?

A high level language can be compiled into an intermediate representation which can be ran on a platform agnostic
virtual machine.

This project can take this intermediate representation and output valid Hack Assembly code, as documented within the
[Hack Assembler](https://github.com/AlanFoster/hackassembler). This output can be converted into its binary
representation using the Hack Assembler, and loaded on to its ROM and executed.

The virtual machine used within this project is modeled after the Java Virtual Machine (JVM).

## Hack Tooling

This project is part of a larger suite of tools:

- [Hack Assembler](https://github.com/AlanFoster/hackassembler) - A basic assembler for the Hack symbolic assembly
  language written in Go.
- [Hack Virtual Machine Translator](https://github.com/AlanFoster/hackassembler) - A virtual machine translator
  for the hack assembly language written with [Antlr](https://www.antlr.org/) and Python.

## Supported functionality

Example virtual machine input code:

```
// Computes the sum 1 + 2 + ... + argument[0] and pushes the
// result onto the stack.
push constant 0
pop local 0         // initializes sum = 0
label LOOP_START
push argument 0
push local 0
add
pop local 0	        // sum = sum + counter
push argument 0
push constant 1
sub
pop argument 0      // counter--
push argument 0
if-goto LOOP_START  // If counter > 0, goto LOOP_START
push local 0
```

This will output symbolic Hack Assembly code, as documented by
[Hack Assembler](https://github.com/AlanFoster/hackassembler). This output can be converted into its binary
representation using the Hack Assembler.

The complete grammar is documented within [VM.g4](./VM.g4)

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

### Run tests

```bash
docker-compose build
docker-compose run --rm test
```
