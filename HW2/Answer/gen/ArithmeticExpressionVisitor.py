# Generated from C:/Users/ASUS/Desktop/term6/Compiler/hw2classver0/2/Simple-Calculator/grammar/ArithmeticExpression.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ArithmeticExpressionParser import ArithmeticExpressionParser
else:
    from ArithmeticExpressionParser import ArithmeticExpressionParser

# This class defines a complete generic visitor for a parse tree produced by ArithmeticExpressionParser.

class ArithmeticExpressionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ArithmeticExpressionParser#start.
    def visitStart(self, ctx:ArithmeticExpressionParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#assigns.
    def visitAssigns(self, ctx:ArithmeticExpressionParser.AssignsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#assign.
    def visitAssign(self, ctx:ArithmeticExpressionParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#expr.
    def visitExpr(self, ctx:ArithmeticExpressionParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#term.
    def visitTerm(self, ctx:ArithmeticExpressionParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#factor_is_string.
    def visitFactor_is_string(self, ctx:ArithmeticExpressionParser.Factor_is_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#factor_is_integer.
    def visitFactor_is_integer(self, ctx:ArithmeticExpressionParser.Factor_is_integerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#factor_is_float.
    def visitFactor_is_float(self, ctx:ArithmeticExpressionParser.Factor_is_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#factor_is_expression.
    def visitFactor_is_expression(self, ctx:ArithmeticExpressionParser.Factor_is_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#factor_is_id.
    def visitFactor_is_id(self, ctx:ArithmeticExpressionParser.Factor_is_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#sign.
    def visitSign(self, ctx:ArithmeticExpressionParser.SignContext):
        return self.visitChildren(ctx)



del ArithmeticExpressionParser