# Generated from VM.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\37")
        buf.write("e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\2\3\3\7\3+\n\3\f\3\16\3.\13\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4:\n\4\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\23\2\2\24\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$\2\5\3\2\6\b\3\2\t\16\3\2\17\26\2\\\2&\3\2\2\2\4,\3\2")
        buf.write("\2\2\69\3\2\2\2\b;\3\2\2\2\n?\3\2\2\2\fC\3\2\2\2\16E\3")
        buf.write("\2\2\2\20G\3\2\2\2\22I\3\2\2\2\24L\3\2\2\2\26O\3\2\2\2")
        buf.write("\30R\3\2\2\2\32T\3\2\2\2\34X\3\2\2\2\36Z\3\2\2\2 ^\3\2")
        buf.write("\2\2\"`\3\2\2\2$b\3\2\2\2&\'\5\4\3\2\'(\7\2\2\3(\3\3\2")
        buf.write("\2\2)+\5\6\4\2*)\3\2\2\2+.\3\2\2\2,*\3\2\2\2,-\3\2\2\2")
        buf.write("-\5\3\2\2\2.,\3\2\2\2/:\5\b\5\2\60:\5\n\6\2\61:\5\f\7")
        buf.write("\2\62:\5\16\b\2\63:\5\26\f\2\64:\5\22\n\2\65:\5\24\13")
        buf.write("\2\66:\5\32\16\2\67:\5\36\20\28:\5$\23\29/\3\2\2\29\60")
        buf.write("\3\2\2\29\61\3\2\2\29\62\3\2\2\29\63\3\2\2\29\64\3\2\2")
        buf.write("\29\65\3\2\2\29\66\3\2\2\29\67\3\2\2\298\3\2\2\2:\7\3")
        buf.write("\2\2\2;<\7\4\2\2<=\5\20\t\2=>\7\3\2\2>\t\3\2\2\2?@\7\5")
        buf.write("\2\2@A\5\20\t\2AB\7\3\2\2B\13\3\2\2\2CD\t\2\2\2D\r\3\2")
        buf.write("\2\2EF\t\3\2\2F\17\3\2\2\2GH\t\4\2\2H\21\3\2\2\2IJ\7\30")
        buf.write("\2\2JK\5\30\r\2K\23\3\2\2\2LM\7\31\2\2MN\5\30\r\2N\25")
        buf.write("\3\2\2\2OP\7\27\2\2PQ\5\30\r\2Q\27\3\2\2\2RS\7\35\2\2")
        buf.write("S\31\3\2\2\2TU\7\32\2\2UV\5 \21\2VW\5\34\17\2W\33\3\2")
        buf.write("\2\2XY\7\3\2\2Y\35\3\2\2\2Z[\7\33\2\2[\\\5 \21\2\\]\5")
        buf.write("\"\22\2]\37\3\2\2\2^_\7\35\2\2_!\3\2\2\2`a\7\3\2\2a#\3")
        buf.write("\2\2\2bc\7\34\2\2c%\3\2\2\2\4,9")
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
                      "LABEL", "GOTO", "IF_GOTO", "CALL", "FUNCTION", "RETURN", 
                      "IDENTIFIER", "COMMENT", "WS" ]

    RULE_program = 0
    RULE_statements = 1
    RULE_statement = 2
    RULE_push = 3
    RULE_pop = 4
    RULE_arithmetic = 5
    RULE_logical = 6
    RULE_segment = 7
    RULE_goto = 8
    RULE_ifGoto = 9
    RULE_label = 10
    RULE_labelIdentifier = 11
    RULE_call = 12
    RULE_argumentCount = 13
    RULE_function = 14
    RULE_functionName = 15
    RULE_localVariableCount = 16
    RULE_returnStatement = 17

    ruleNames =  [ "program", "statements", "statement", "push", "pop", 
                   "arithmetic", "logical", "segment", "goto", "ifGoto", 
                   "label", "labelIdentifier", "call", "argumentCount", 
                   "function", "functionName", "localVariableCount", "returnStatement" ]

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
    LABEL=21
    GOTO=22
    IF_GOTO=23
    CALL=24
    FUNCTION=25
    RETURN=26
    IDENTIFIER=27
    COMMENT=28
    WS=29

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
            self.state = 36
            self.statements()
            self.state = 37
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
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VMParser.PUSH) | (1 << VMParser.POP) | (1 << VMParser.ADD) | (1 << VMParser.SUB) | (1 << VMParser.NEG) | (1 << VMParser.LT) | (1 << VMParser.EQ) | (1 << VMParser.GT) | (1 << VMParser.AND) | (1 << VMParser.OR) | (1 << VMParser.NOT) | (1 << VMParser.LABEL) | (1 << VMParser.GOTO) | (1 << VMParser.IF_GOTO) | (1 << VMParser.CALL) | (1 << VMParser.FUNCTION) | (1 << VMParser.RETURN))) != 0):
                self.state = 39
                self.statement()
                self.state = 44
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


        def label(self):
            return self.getTypedRuleContext(VMParser.LabelContext,0)


        def goto(self):
            return self.getTypedRuleContext(VMParser.GotoContext,0)


        def ifGoto(self):
            return self.getTypedRuleContext(VMParser.IfGotoContext,0)


        def call(self):
            return self.getTypedRuleContext(VMParser.CallContext,0)


        def function(self):
            return self.getTypedRuleContext(VMParser.FunctionContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(VMParser.ReturnStatementContext,0)


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
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VMParser.PUSH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.push()
                pass
            elif token in [VMParser.POP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.pop()
                pass
            elif token in [VMParser.ADD, VMParser.SUB, VMParser.NEG]:
                self.enterOuterAlt(localctx, 3)
                self.state = 47
                self.arithmetic()
                pass
            elif token in [VMParser.LT, VMParser.EQ, VMParser.GT, VMParser.AND, VMParser.OR, VMParser.NOT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                self.logical()
                pass
            elif token in [VMParser.LABEL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 49
                self.label()
                pass
            elif token in [VMParser.GOTO]:
                self.enterOuterAlt(localctx, 6)
                self.state = 50
                self.goto()
                pass
            elif token in [VMParser.IF_GOTO]:
                self.enterOuterAlt(localctx, 7)
                self.state = 51
                self.ifGoto()
                pass
            elif token in [VMParser.CALL]:
                self.enterOuterAlt(localctx, 8)
                self.state = 52
                self.call()
                pass
            elif token in [VMParser.FUNCTION]:
                self.enterOuterAlt(localctx, 9)
                self.state = 53
                self.function()
                pass
            elif token in [VMParser.RETURN]:
                self.enterOuterAlt(localctx, 10)
                self.state = 54
                self.returnStatement()
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
            self.state = 57
            self.match(VMParser.PUSH)
            self.state = 58
            self.segment()
            self.state = 59
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
            self.state = 61
            self.match(VMParser.POP)
            self.state = 62
            self.segment()
            self.state = 63
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
            self.state = 65
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
            self.state = 67
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
            self.state = 69
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


    class GotoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GOTO(self):
            return self.getToken(VMParser.GOTO, 0)

        def labelIdentifier(self):
            return self.getTypedRuleContext(VMParser.LabelIdentifierContext,0)


        def getRuleIndex(self):
            return VMParser.RULE_goto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoto" ):
                listener.enterGoto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoto" ):
                listener.exitGoto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGoto" ):
                return visitor.visitGoto(self)
            else:
                return visitor.visitChildren(self)




    def goto(self):

        localctx = VMParser.GotoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_goto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(VMParser.GOTO)
            self.state = 72
            self.labelIdentifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfGotoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_GOTO(self):
            return self.getToken(VMParser.IF_GOTO, 0)

        def labelIdentifier(self):
            return self.getTypedRuleContext(VMParser.LabelIdentifierContext,0)


        def getRuleIndex(self):
            return VMParser.RULE_ifGoto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfGoto" ):
                listener.enterIfGoto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfGoto" ):
                listener.exitIfGoto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfGoto" ):
                return visitor.visitIfGoto(self)
            else:
                return visitor.visitChildren(self)




    def ifGoto(self):

        localctx = VMParser.IfGotoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifGoto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(VMParser.IF_GOTO)
            self.state = 75
            self.labelIdentifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LABEL(self):
            return self.getToken(VMParser.LABEL, 0)

        def labelIdentifier(self):
            return self.getTypedRuleContext(VMParser.LabelIdentifierContext,0)


        def getRuleIndex(self):
            return VMParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = VMParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(VMParser.LABEL)
            self.state = 78
            self.labelIdentifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelIdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(VMParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return VMParser.RULE_labelIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelIdentifier" ):
                listener.enterLabelIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelIdentifier" ):
                listener.exitLabelIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabelIdentifier" ):
                return visitor.visitLabelIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def labelIdentifier(self):

        localctx = VMParser.LabelIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_labelIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(VMParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CALL(self):
            return self.getToken(VMParser.CALL, 0)

        def functionName(self):
            return self.getTypedRuleContext(VMParser.FunctionNameContext,0)


        def argumentCount(self):
            return self.getTypedRuleContext(VMParser.ArgumentCountContext,0)


        def getRuleIndex(self):
            return VMParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = VMParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(VMParser.CALL)
            self.state = 83
            self.functionName()
            self.state = 84
            self.argumentCount()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentCountContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(VMParser.INT, 0)

        def getRuleIndex(self):
            return VMParser.RULE_argumentCount

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentCount" ):
                listener.enterArgumentCount(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentCount" ):
                listener.exitArgumentCount(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentCount" ):
                return visitor.visitArgumentCount(self)
            else:
                return visitor.visitChildren(self)




    def argumentCount(self):

        localctx = VMParser.ArgumentCountContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_argumentCount)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(VMParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(VMParser.FUNCTION, 0)

        def functionName(self):
            return self.getTypedRuleContext(VMParser.FunctionNameContext,0)


        def localVariableCount(self):
            return self.getTypedRuleContext(VMParser.LocalVariableCountContext,0)


        def getRuleIndex(self):
            return VMParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = VMParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(VMParser.FUNCTION)
            self.state = 89
            self.functionName()
            self.state = 90
            self.localVariableCount()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(VMParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return VMParser.RULE_functionName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionName" ):
                listener.enterFunctionName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionName" ):
                listener.exitFunctionName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionName" ):
                return visitor.visitFunctionName(self)
            else:
                return visitor.visitChildren(self)




    def functionName(self):

        localctx = VMParser.FunctionNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_functionName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(VMParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocalVariableCountContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(VMParser.INT, 0)

        def getRuleIndex(self):
            return VMParser.RULE_localVariableCount

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocalVariableCount" ):
                listener.enterLocalVariableCount(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocalVariableCount" ):
                listener.exitLocalVariableCount(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocalVariableCount" ):
                return visitor.visitLocalVariableCount(self)
            else:
                return visitor.visitChildren(self)




    def localVariableCount(self):

        localctx = VMParser.LocalVariableCountContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_localVariableCount)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(VMParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(VMParser.RETURN, 0)

        def getRuleIndex(self):
            return VMParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = VMParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(VMParser.RETURN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





