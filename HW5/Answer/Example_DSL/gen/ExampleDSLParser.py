# Generated from C:/PHD_Projects/Example_DSL/grammar/ExampleDSL.g4 by ANTLR 4.13.1
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
        4,1,10,60,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,1,3,1,27,8,1,1,
        1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,
        6,1,7,1,7,4,7,48,8,7,11,7,12,7,49,1,8,1,8,1,8,1,8,1,9,1,9,1,10,1,
        10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,1,1,0,2,3,50,0,22,1,
        0,0,0,2,26,1,0,0,0,4,31,1,0,0,0,6,34,1,0,0,0,8,36,1,0,0,0,10,41,
        1,0,0,0,12,43,1,0,0,0,14,47,1,0,0,0,16,51,1,0,0,0,18,55,1,0,0,0,
        20,57,1,0,0,0,22,23,3,2,1,0,23,24,5,0,0,1,24,1,1,0,0,0,25,27,3,4,
        2,0,26,25,1,0,0,0,26,27,1,0,0,0,27,28,1,0,0,0,28,29,3,8,4,0,29,30,
        3,14,7,0,30,3,1,0,0,0,31,32,5,1,0,0,32,33,3,6,3,0,33,5,1,0,0,0,34,
        35,7,0,0,0,35,7,1,0,0,0,36,37,5,4,0,0,37,38,3,10,5,0,38,39,5,5,0,
        0,39,40,3,12,6,0,40,9,1,0,0,0,41,42,5,8,0,0,42,11,1,0,0,0,43,44,
        5,8,0,0,44,13,1,0,0,0,45,46,5,6,0,0,46,48,3,16,8,0,47,45,1,0,0,0,
        48,49,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,15,1,0,0,0,51,52,3,
        18,9,0,52,53,5,7,0,0,53,54,3,20,10,0,54,17,1,0,0,0,55,56,5,8,0,0,
        56,19,1,0,0,0,57,58,5,8,0,0,58,21,1,0,0,0,2,26,49
    ]

class ExampleDSLParser ( Parser ):

    grammarFileName = "ExampleDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'output:'", "'html'", "'console'", "'game:'", 
                     "'X'", "'bomb:'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INTEGER", "WS", "NEWLINE" ]

    RULE_start = 0
    RULE_program = 1
    RULE_output = 2
    RULE_output_types = 3
    RULE_initiate_game = 4
    RULE_width = 5
    RULE_height = 6
    RULE_bomb_placements = 7
    RULE_bomb_location = 8
    RULE_x_location = 9
    RULE_y_location = 10

    ruleNames =  [ "start", "program", "output", "output_types", "initiate_game", 
                   "width", "height", "bomb_placements", "bomb_location", 
                   "x_location", "y_location" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    INTEGER=8
    WS=9
    NEWLINE=10

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

        def program(self):
            return self.getTypedRuleContext(ExampleDSLParser.ProgramContext,0)


        def EOF(self):
            return self.getToken(ExampleDSLParser.EOF, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_start

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

        localctx = ExampleDSLParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.program()
            self.state = 23
            self.match(ExampleDSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initiate_game(self):
            return self.getTypedRuleContext(ExampleDSLParser.Initiate_gameContext,0)


        def bomb_placements(self):
            return self.getTypedRuleContext(ExampleDSLParser.Bomb_placementsContext,0)


        def output(self):
            return self.getTypedRuleContext(ExampleDSLParser.OutputContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_program

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

        localctx = ExampleDSLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 25
                self.output()


            self.state = 28
            self.initiate_game()
            self.state = 29
            self.bomb_placements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def output_types(self):
            return self.getTypedRuleContext(ExampleDSLParser.Output_typesContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_output

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutput" ):
                listener.enterOutput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutput" ):
                listener.exitOutput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutput" ):
                return visitor.visitOutput(self)
            else:
                return visitor.visitChildren(self)




    def output(self):

        localctx = ExampleDSLParser.OutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_output)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(ExampleDSLParser.T__0)
            self.state = 32
            self.output_types()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Output_typesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_output_types

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutput_types" ):
                listener.enterOutput_types(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutput_types" ):
                listener.exitOutput_types(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutput_types" ):
                return visitor.visitOutput_types(self)
            else:
                return visitor.visitChildren(self)




    def output_types(self):

        localctx = ExampleDSLParser.Output_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_output_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
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


    class Initiate_gameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def width(self):
            return self.getTypedRuleContext(ExampleDSLParser.WidthContext,0)


        def height(self):
            return self.getTypedRuleContext(ExampleDSLParser.HeightContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_initiate_game

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitiate_game" ):
                listener.enterInitiate_game(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitiate_game" ):
                listener.exitInitiate_game(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitiate_game" ):
                return visitor.visitInitiate_game(self)
            else:
                return visitor.visitChildren(self)




    def initiate_game(self):

        localctx = ExampleDSLParser.Initiate_gameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_initiate_game)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(ExampleDSLParser.T__3)
            self.state = 37
            self.width()
            self.state = 38
            self.match(ExampleDSLParser.T__4)
            self.state = 39
            self.height()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WidthContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(ExampleDSLParser.INTEGER, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_width

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWidth" ):
                listener.enterWidth(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWidth" ):
                listener.exitWidth(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWidth" ):
                return visitor.visitWidth(self)
            else:
                return visitor.visitChildren(self)




    def width(self):

        localctx = ExampleDSLParser.WidthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_width)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(ExampleDSLParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeightContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(ExampleDSLParser.INTEGER, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_height

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeight" ):
                listener.enterHeight(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeight" ):
                listener.exitHeight(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeight" ):
                return visitor.visitHeight(self)
            else:
                return visitor.visitChildren(self)




    def height(self):

        localctx = ExampleDSLParser.HeightContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_height)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(ExampleDSLParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bomb_placementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bomb_location(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExampleDSLParser.Bomb_locationContext)
            else:
                return self.getTypedRuleContext(ExampleDSLParser.Bomb_locationContext,i)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_bomb_placements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBomb_placements" ):
                listener.enterBomb_placements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBomb_placements" ):
                listener.exitBomb_placements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBomb_placements" ):
                return visitor.visitBomb_placements(self)
            else:
                return visitor.visitChildren(self)




    def bomb_placements(self):

        localctx = ExampleDSLParser.Bomb_placementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_bomb_placements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 45
                self.match(ExampleDSLParser.T__5)
                self.state = 46
                self.bomb_location()
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==6):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bomb_locationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def x_location(self):
            return self.getTypedRuleContext(ExampleDSLParser.X_locationContext,0)


        def y_location(self):
            return self.getTypedRuleContext(ExampleDSLParser.Y_locationContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_bomb_location

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBomb_location" ):
                listener.enterBomb_location(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBomb_location" ):
                listener.exitBomb_location(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBomb_location" ):
                return visitor.visitBomb_location(self)
            else:
                return visitor.visitChildren(self)




    def bomb_location(self):

        localctx = ExampleDSLParser.Bomb_locationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_bomb_location)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.x_location()
            self.state = 52
            self.match(ExampleDSLParser.T__6)
            self.state = 53
            self.y_location()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class X_locationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(ExampleDSLParser.INTEGER, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_x_location

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterX_location" ):
                listener.enterX_location(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitX_location" ):
                listener.exitX_location(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitX_location" ):
                return visitor.visitX_location(self)
            else:
                return visitor.visitChildren(self)




    def x_location(self):

        localctx = ExampleDSLParser.X_locationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_x_location)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(ExampleDSLParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Y_locationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(ExampleDSLParser.INTEGER, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_y_location

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterY_location" ):
                listener.enterY_location(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitY_location" ):
                listener.exitY_location(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitY_location" ):
                return visitor.visitY_location(self)
            else:
                return visitor.visitChildren(self)




    def y_location(self):

        localctx = ExampleDSLParser.Y_locationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_y_location)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(ExampleDSLParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





