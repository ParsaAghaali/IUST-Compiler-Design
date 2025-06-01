# Generated from C:/Users/ASUS/Desktop/term6/Compiler/hw1/First_Homework/First_excercise/Simple-Calculator/grammar/ArithmeticExpression.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,70,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,23,8,1,1,2,1,2,1,2,1,2,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,38,8,3,10,3,12,3,41,9,3,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,52,8,4,10,4,12,4,55,9,4,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,66,8,5,1,6,1,6,1,6,0,2,6,8,7,
        0,2,4,6,8,10,12,0,0,71,0,14,1,0,0,0,2,22,1,0,0,0,4,24,1,0,0,0,6,
        28,1,0,0,0,8,42,1,0,0,0,10,65,1,0,0,0,12,67,1,0,0,0,14,15,3,2,1,
        0,15,16,5,0,0,1,16,1,1,0,0,0,17,18,3,4,2,0,18,19,5,11,0,0,19,20,
        3,2,1,0,20,23,1,0,0,0,21,23,3,4,2,0,22,17,1,0,0,0,22,21,1,0,0,0,
        23,3,1,0,0,0,24,25,5,12,0,0,25,26,5,1,0,0,26,27,3,6,3,0,27,5,1,0,
        0,0,28,29,6,3,-1,0,29,30,3,8,4,0,30,39,1,0,0,0,31,32,10,3,0,0,32,
        33,5,2,0,0,33,38,3,8,4,0,34,35,10,2,0,0,35,36,5,3,0,0,36,38,3,8,
        4,0,37,31,1,0,0,0,37,34,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,
        1,0,0,0,40,7,1,0,0,0,41,39,1,0,0,0,42,43,6,4,-1,0,43,44,3,10,5,0,
        44,53,1,0,0,0,45,46,10,3,0,0,46,47,5,4,0,0,47,52,3,10,5,0,48,49,
        10,2,0,0,49,50,5,5,0,0,50,52,3,10,5,0,51,45,1,0,0,0,51,48,1,0,0,
        0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,9,1,0,0,0,55,53,1,
        0,0,0,56,66,3,12,6,0,57,58,5,2,0,0,58,66,3,12,6,0,59,60,5,6,0,0,
        60,61,3,6,3,0,61,62,5,7,0,0,62,66,1,0,0,0,63,66,5,9,0,0,64,66,5,
        12,0,0,65,56,1,0,0,0,65,57,1,0,0,0,65,59,1,0,0,0,65,63,1,0,0,0,65,
        64,1,0,0,0,66,11,1,0,0,0,67,68,5,8,0,0,68,13,1,0,0,0,6,22,37,39,
        51,53,65
    ]

class ArithmeticExpressionParser ( Parser ):

    grammarFileName = "ArithmeticExpression.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+'", "'-'", "'*'", "'/'", "'('", 
                     "')'", "<INVALID>", "<INVALID>", "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "ADD", "SUB", "MUL", "DIV", 
                      "LPAREN", "RPAREN", "NUMERICALVALUE", "STRING", "WS", 
                      "NEWLINE", "ID" ]

    RULE_start = 0
    RULE_assigns = 1
    RULE_assign = 2
    RULE_expr = 3
    RULE_term = 4
    RULE_factor = 5
    RULE_number = 6

    ruleNames =  [ "start", "assigns", "assign", "expr", "term", "factor", 
                   "number" ]

    EOF = Token.EOF
    T__0=1
    ADD=2
    SUB=3
    MUL=4
    DIV=5
    LPAREN=6
    RPAREN=7
    NUMERICALVALUE=8
    STRING=9
    WS=10
    NEWLINE=11
    ID=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assigns(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.AssignsContext,0)


        def EOF(self):
            return self.getToken(ArithmeticExpressionParser.EOF, 0)

        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = ArithmeticExpressionParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.assigns()
            self.state = 15
            self.match(ArithmeticExpressionParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.AssignContext,0)


        def NEWLINE(self):
            return self.getToken(ArithmeticExpressionParser.NEWLINE, 0)

        def assigns(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.AssignsContext,0)


        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_assigns

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssigns" ):
                listener.enterAssigns(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssigns" ):
                listener.exitAssigns(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssigns" ):
                return visitor.visitAssigns(self)
            else:
                return visitor.visitChildren(self)




    def assigns(self):

        localctx = ArithmeticExpressionParser.AssignsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_assigns)
        try:
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.assign()
                self.state = 18
                self.match(ArithmeticExpressionParser.NEWLINE)
                self.state = 19
                self.assigns()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.assign()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ArithmeticExpressionParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.ExprContext,0)


        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = ArithmeticExpressionParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(ArithmeticExpressionParser.ID)
            self.state = 25
            self.match(ArithmeticExpressionParser.T__0)
            self.state = 26
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def term(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.TermContext,0)


        def expr(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.ExprContext,0)


        def ADD(self):
            return self.getToken(ArithmeticExpressionParser.ADD, 0)

        def SUB(self):
            return self.getToken(ArithmeticExpressionParser.SUB, 0)

        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ArithmeticExpressionParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 37
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ArithmeticExpressionParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 32
                        localctx.op = self.match(ArithmeticExpressionParser.ADD)
                        self.state = 33
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = ArithmeticExpressionParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 35
                        self.match(ArithmeticExpressionParser.SUB)
                        self.state = 36
                        self.term(0)
                        pass

             
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.TermContext,0)


        def MUL(self):
            return self.getToken(ArithmeticExpressionParser.MUL, 0)

        def DIV(self):
            return self.getToken(ArithmeticExpressionParser.DIV, 0)

        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ArithmeticExpressionParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 51
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ArithmeticExpressionParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 45
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 46
                        self.match(ArithmeticExpressionParser.MUL)
                        self.state = 47
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = ArithmeticExpressionParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 48
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 49
                        self.match(ArithmeticExpressionParser.DIV)
                        self.state = 50
                        self.factor()
                        pass

             
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.NumberContext,0)


        def ADD(self):
            return self.getToken(ArithmeticExpressionParser.ADD, 0)

        def LPAREN(self):
            return self.getToken(ArithmeticExpressionParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ArithmeticExpressionParser.RPAREN, 0)

        def STRING(self):
            return self.getToken(ArithmeticExpressionParser.STRING, 0)

        def ID(self):
            return self.getToken(ArithmeticExpressionParser.ID, 0)

        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = ArithmeticExpressionParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_factor)
        try:
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.number()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.match(ArithmeticExpressionParser.ADD)
                self.state = 58
                self.number()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.match(ArithmeticExpressionParser.LPAREN)
                self.state = 60
                self.expr(0)
                self.state = 61
                self.match(ArithmeticExpressionParser.RPAREN)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 63
                self.match(ArithmeticExpressionParser.STRING)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 64
                self.match(ArithmeticExpressionParser.ID)
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


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERICALVALUE(self):
            return self.getToken(ArithmeticExpressionParser.NUMERICALVALUE, 0)

        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = ArithmeticExpressionParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(ArithmeticExpressionParser.NUMERICALVALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        self._predicates[4] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




