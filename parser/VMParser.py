# Generated from VM.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("\60\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write("\b\t\b\4\t\t\t\3\2\3\2\3\2\3\3\7\3\27\n\3\f\3\16\3\32")
        buf.write("\13\3\3\4\3\4\3\4\3\4\5\4 \n\4\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\2\2\n\2\4\6\b\n\f")
        buf.write("\16\20\2\5\3\2\6\b\3\2\t\16\3\2\17\26\2+\2\22\3\2\2\2")
        buf.write("\4\30\3\2\2\2\6\37\3\2\2\2\b!\3\2\2\2\n%\3\2\2\2\f)\3")
        buf.write("\2\2\2\16+\3\2\2\2\20-\3\2\2\2\22\23\5\4\3\2\23\24\7\2")
        buf.write("\2\3\24\3\3\2\2\2\25\27\5\6\4\2\26\25\3\2\2\2\27\32\3")
        buf.write("\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31\5\3\2\2\2\32\30")
        buf.write("\3\2\2\2\33 \5\b\5\2\34 \5\n\6\2\35 \5\f\7\2\36 \5\16")
        buf.write("\b\2\37\33\3\2\2\2\37\34\3\2\2\2\37\35\3\2\2\2\37\36\3")
        buf.write("\2\2\2 \7\3\2\2\2!\"\7\4\2\2\"#\5\20\t\2#$\7\3\2\2$\t")
        buf.write("\3\2\2\2%&\7\5\2\2&\'\5\20\t\2\'(\7\3\2\2(\13\3\2\2\2")
        buf.write(")*\t\2\2\2*\r\3\2\2\2+,\t\3\2\2,\17\3\2\2\2-.\t\4\2\2")
        buf.write(".\21\3\2\2\2\4\30\37")
        return buf.getvalue()


class VMParser ( Parser ):

    grammarFileName = "VM.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "INT", "PUSH", "POP", "ADD", "SUB", "NEG", 
                      "LT", "EQ", "GT", "AND", "OR", "NOT", "LOCAL", "ARGUMENT", 
                      "THIS", "THAT", "CONSTANT", "STATIC", "POINTER", "TEMP", 
                      "COMMENT", "WS" ]

    RULE_program = 0
    RULE_statements = 1
    RULE_statement = 2
    RULE_push = 3
    RULE_pop = 4
    RULE_arithmetic = 5
    RULE_logical = 6
    RULE_segment = 7

    ruleNames =  [ "program", "statements", "statement", "push", "pop", 
                   "arithmetic", "logical", "segment" ]

    EOF = Token.EOF
    INT=1
    PUSH=2
    POP=3
    ADD=4
    SUB=5
    NEG=6
    LT=7
    EQ=8
    GT=9
    AND=10
    OR=11
    NOT=12
    LOCAL=13
    ARGUMENT=14
    THIS=15
    THAT=16
    CONSTANT=17
    STATIC=18
    POINTER=19
    TEMP=20
    COMMENT=21
    WS=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(VMParser.StatementsContext,0)


        def EOF(self):
            return self.getToken(VMParser.EOF, 0)

        def getRuleIndex(self):
            return VMParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = VMParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.statements()
            self.state = 17
            self.match(VMParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VMParser.StatementContext)
            else:
                return self.getTypedRuleContext(VMParser.StatementContext,i)


        def getRuleIndex(self):
            return VMParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = VMParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VMParser.PUSH) | (1 << VMParser.POP) | (1 << VMParser.ADD) | (1 << VMParser.SUB) | (1 << VMParser.NEG) | (1 << VMParser.LT) | (1 << VMParser.EQ) | (1 << VMParser.GT) | (1 << VMParser.AND) | (1 << VMParser.OR) | (1 << VMParser.NOT))) != 0):
                self.state = 19
                self.statement()
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def push(self):
            return self.getTypedRuleContext(VMParser.PushContext,0)


        def pop(self):
            return self.getTypedRuleContext(VMParser.PopContext,0)


        def arithmetic(self):
            return self.getTypedRuleContext(VMParser.ArithmeticContext,0)


        def logical(self):
            return self.getTypedRuleContext(VMParser.LogicalContext,0)


        def getRuleIndex(self):
            return VMParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = VMParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VMParser.PUSH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.push()
                pass
            elif token in [VMParser.POP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.pop()
                pass
            elif token in [VMParser.ADD, VMParser.SUB, VMParser.NEG]:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.arithmetic()
                pass
            elif token in [VMParser.LT, VMParser.EQ, VMParser.GT, VMParser.AND, VMParser.OR, VMParser.NOT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.logical()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PushContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUSH(self):
            return self.getToken(VMParser.PUSH, 0)

        def segment(self):
            return self.getTypedRuleContext(VMParser.SegmentContext,0)


        def INT(self):
            return self.getToken(VMParser.INT, 0)

        def getRuleIndex(self):
            return VMParser.RULE_push

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPush" ):
                listener.enterPush(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPush" ):
                listener.exitPush(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPush" ):
                return visitor.visitPush(self)
            else:
                return visitor.visitChildren(self)




    def push(self):

        localctx = VMParser.PushContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_push)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(VMParser.PUSH)
            self.state = 32
            self.segment()
            self.state = 33
            self.match(VMParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POP(self):
            return self.getToken(VMParser.POP, 0)

        def segment(self):
            return self.getTypedRuleContext(VMParser.SegmentContext,0)


        def INT(self):
            return self.getToken(VMParser.INT, 0)

        def getRuleIndex(self):
            return VMParser.RULE_pop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPop" ):
                listener.enterPop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPop" ):
                listener.exitPop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPop" ):
                return visitor.visitPop(self)
            else:
                return visitor.visitChildren(self)




    def pop(self):

        localctx = VMParser.PopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_pop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(VMParser.POP)
            self.state = 36
            self.segment()
            self.state = 37
            self.match(VMParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(VMParser.ADD, 0)

        def SUB(self):
            return self.getToken(VMParser.SUB, 0)

        def NEG(self):
            return self.getToken(VMParser.NEG, 0)

        def getRuleIndex(self):
            return VMParser.RULE_arithmetic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic" ):
                listener.enterArithmetic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic" ):
                listener.exitArithmetic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic" ):
                return visitor.visitArithmetic(self)
            else:
                return visitor.visitChildren(self)




    def arithmetic(self):

        localctx = VMParser.ArithmeticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arithmetic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VMParser.ADD) | (1 << VMParser.SUB) | (1 << VMParser.NEG))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(VMParser.LT, 0)

        def EQ(self):
            return self.getToken(VMParser.EQ, 0)

        def GT(self):
            return self.getToken(VMParser.GT, 0)

        def AND(self):
            return self.getToken(VMParser.AND, 0)

        def OR(self):
            return self.getToken(VMParser.OR, 0)

        def NOT(self):
            return self.getToken(VMParser.NOT, 0)

        def getRuleIndex(self):
            return VMParser.RULE_logical

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical" ):
                listener.enterLogical(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical" ):
                listener.exitLogical(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical" ):
                return visitor.visitLogical(self)
            else:
                return visitor.visitChildren(self)




    def logical(self):

        localctx = VMParser.LogicalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VMParser.LT) | (1 << VMParser.EQ) | (1 << VMParser.GT) | (1 << VMParser.AND) | (1 << VMParser.OR) | (1 << VMParser.NOT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SegmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOCAL(self):
            return self.getToken(VMParser.LOCAL, 0)

        def ARGUMENT(self):
            return self.getToken(VMParser.ARGUMENT, 0)

        def THIS(self):
            return self.getToken(VMParser.THIS, 0)

        def THAT(self):
            return self.getToken(VMParser.THAT, 0)

        def CONSTANT(self):
            return self.getToken(VMParser.CONSTANT, 0)

        def STATIC(self):
            return self.getToken(VMParser.STATIC, 0)

        def POINTER(self):
            return self.getToken(VMParser.POINTER, 0)

        def TEMP(self):
            return self.getToken(VMParser.TEMP, 0)

        def getRuleIndex(self):
            return VMParser.RULE_segment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSegment" ):
                listener.enterSegment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSegment" ):
                listener.exitSegment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSegment" ):
                return visitor.visitSegment(self)
            else:
                return visitor.visitChildren(self)




    def segment(self):

        localctx = VMParser.SegmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_segment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VMParser.LOCAL) | (1 << VMParser.ARGUMENT) | (1 << VMParser.THIS) | (1 << VMParser.THAT) | (1 << VMParser.CONSTANT) | (1 << VMParser.STATIC) | (1 << VMParser.POINTER) | (1 << VMParser.TEMP))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





