# Generated from C:/Users/ASUS/Desktop/term6/Compiler/hw2classver0/2/Simple-Calculator/grammar/ArithmeticExpression.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ArithmeticExpressionParser import ArithmeticExpressionParser
else:
    from ArithmeticExpressionParser import ArithmeticExpressionParser

# This class defines a complete listener for a parse tree produced by ArithmeticExpressionParser.
class ArithmeticExpressionListener(ParseTreeListener):

    # Enter a parse tree produced by ArithmeticExpressionParser#start.
    def enterStart(self, ctx:ArithmeticExpressionParser.StartContext):
        pass

    # Exit a parse tree produced by ArithmeticExpressionParser#start.
    def exitStart(self, ctx:ArithmeticExpressionParser.StartContext):
        pass


    # Enter a parse tree produced by ArithmeticExpressionParser#assigns.
    def enterAssigns(self, ctx:ArithmeticExpressionParser.AssignsContext):
        pass

    # Exit a parse tree produced by ArithmeticExpressionParser#assigns.
    def exitAssigns(self, ctx:ArithmeticExpressionParser.AssignsContext):
        pass


    # Enter a parse tree produced by ArithmeticExpressionParser#assign.
    def enterAssign(self, ctx:ArithmeticExpressionParser.AssignContext):
        pass

    # Exit a parse tree produced by ArithmeticExpressionParser#assign.
    def exitAssign(self, ctx:ArithmeticExpressionParser.AssignContext):
        pass


    # Enter a parse tree produced by ArithmeticExpressionParser#expr.
    def enterExpr(self, ctx:ArithmeticExpressionParser.ExprContext):
        pass

    # Exit a parse tree produced by ArithmeticExpressionParser#expr.
    def exitExpr(self, ctx:ArithmeticExpressionParser.ExprContext):
        pass


    # Enter a parse tree produced by ArithmeticExpressionParser#term.
    def enterTerm(self, ctx:ArithmeticExpressionParser.TermContext):
        pass

    # Exit a parse tree produced by ArithmeticExpressionParser#term.
    def exitTerm(self, ctx:ArithmeticExpressionParser.TermContext):
        pass


    # Enter a parse tree produced by ArithmeticExpressionParser#factor_is_string.
    def enterFactor_is_string(self, ctx:ArithmeticExpressionParser.Factor_is_stringContext):
        pass

    # Exit a parse tree produced by ArithmeticExpressionParser#factor_is_string.
    def exitFactor_is_string(self, ctx:ArithmeticExpressionParser.Factor_is_stringContext):
        pass


    # Enter a parse tree produced by ArithmeticExpressionParser#factor_is_integer.
    def enterFactor_is_integer(self, ctx:ArithmeticExpressionParser.Factor_is_integerContext):
        pass

    # Exit a parse tree produced by ArithmeticExpressionParser#factor_is_integer.
    def exitFactor_is_integer(self, ctx:ArithmeticExpressionParser.Factor_is_integerContext):
        pass


    # Enter a parse tree produced by ArithmeticExpressionParser#factor_is_float.
    def enterFactor_is_float(self, ctx:ArithmeticExpressionParser.Factor_is_floatContext):
        pass

    # Exit a parse tree produced by ArithmeticExpressionParser#factor_is_float.
    def exitFactor_is_float(self, ctx:ArithmeticExpressionParser.Factor_is_floatContext):
        pass


    # Enter a parse tree produced by ArithmeticExpressionParser#factor_is_expression.
    def enterFactor_is_expression(self, ctx:ArithmeticExpressionParser.Factor_is_expressionContext):
        pass

    # Exit a parse tree produced by ArithmeticExpressionParser#factor_is_expression.
    def exitFactor_is_expression(self, ctx:ArithmeticExpressionParser.Factor_is_expressionContext):
        pass


    # Enter a parse tree produced by ArithmeticExpressionParser#factor_is_id.
    def enterFactor_is_id(self, ctx:ArithmeticExpressionParser.Factor_is_idContext):
        pass

    # Exit a parse tree produced by ArithmeticExpressionParser#factor_is_id.
    def exitFactor_is_id(self, ctx:ArithmeticExpressionParser.Factor_is_idContext):
        pass


    # Enter a parse tree produced by ArithmeticExpressionParser#sign.
    def enterSign(self, ctx:ArithmeticExpressionParser.SignContext):
        pass

    # Exit a parse tree produced by ArithmeticExpressionParser#sign.
    def exitSign(self, ctx:ArithmeticExpressionParser.SignContext):
        pass



del ArithmeticExpressionParser