from gen.ArithmeticExpressionListener import ArithmeticExpressionListener
from gen.ArithmeticExpressionParser import ArithmeticExpressionParser


class CalculatorListener(ArithmeticExpressionListener):

    # Exit a parse tree produced by ArithmeticExpressionParser#assign.
    def exitAssign(self, ctx: ArithmeticExpressionParser.AssignContext):
        print(ctx.getChild(0).getText(), ' is  ===> ', ctx.getChild(2).value)
        print(ctx.getChild(2).rule_type) #type output ctx.getChild(2).rule_type

    # Exit a parse tree produced by ArithmeticExpressionParser#expr_add_op.
    def exitExpr(self, ctx: ArithmeticExpressionParser.ExprContext):
        if ctx.getChildCount() == 1: #if one number in expr: ex. a=9
            ctx.value = ctx.getChild(0).value
            ctx.rule_type = ctx.getChild(0).rule_type
        else:
            operator = ctx.getChild(1).getText()
            if operator == "+":
                left_child_type = ctx.getChild(0).rule_type
                right_child_type = ctx.getChild(2).rule_type
                if left_child_type == "String" and (right_child_type == "Integer"
                                                    or right_child_type == "Float"): #string + int/float
                    ctx.rule_type = "String" #output type is string
                    ctx.value = ctx.getChild(0).value.replace('"', '', 2) + str(ctx.getChild(2).value)
                elif left_child_type == "String" and right_child_type == "String": #String + String
                    ctx.rule_type = "String"
                    ctx.value = ctx.getChild(0).value.replace('"', '', 2) + ctx.getChild(2).value.replace('"', '', 2)
                elif left_child_type == "Integer" and right_child_type == "Integer": #Integer + Integer
                    ctx.rule_type = "Integer"
                    ctx.value = ctx.getChild(0).value + ctx.getChild(2).value
                elif left_child_type == "Integer" and right_child_type == "Float": #Integer + Float
                    ctx.rule_type = "Float"
                    ctx.value = ctx.getChild(0).value + ctx.getChild(2).value
                elif left_child_type == "Float" and right_child_type == "Integer": #Float + Integer
                    ctx.rule_type = "Float"
                    ctx.value = ctx.getChild(0).value + ctx.getChild(2).value
                elif left_child_type == "Float" and right_child_type == "Float": #Float + Float
                    ctx.rule_type = "Float"
                    ctx.value = ctx.getChild(0).value + ctx.getChild(2).value
                elif left_child_type == "Integer" and right_child_type == "String": #Integer + Srting
                    ctx.rule_type = "Error"
                    ctx.value = ""
                elif left_child_type == "Float" and right_child_type == "String": #Float + Srting
                    ctx.rule_type = "Error"
                    ctx.value = ""
                elif left_child_type == "String" and right_child_type == "String": #Float + Srting
                    ctx.rule_type = "Error"
                    ctx.value = ""
                else:
                    ctx.rule_type = "No idea for exitExpr operator == +"
                    ctx.value = "???+"

            elif operator == "-":
                left_child_type = ctx.getChild(0).rule_type
                right_child_type = ctx.getChild(2).rule_type
                if left_child_type == "String" and (right_child_type == "String" or right_child_type == "Integer"
                                                    or right_child_type == "Float"): #String - (String or Integer or Float)
                    ctx.rule_type = "Error"
                    ctx.value = ""
                elif left_child_type == "Integer" and right_child_type == "Integer": #Integer - Integer
                    ctx.rule_type = "Integer"
                    ctx.value = ctx.getChild(0).value - ctx.getChild(2).value
                elif left_child_type == "Integer" and right_child_type == "Float": #Integer - Float
                    ctx.rule_type = "Float"
                    ctx.value = ctx.getChild(0).value - ctx.getChild(2).value
                elif left_child_type == "Float" and right_child_type == "Integer": #Float - Integer
                    ctx.rule_type = "Float"
                    ctx.value = ctx.getChild(0).value - ctx.getChild(2).value
                elif left_child_type == "Float" and right_child_type == "Float": #Float - Float
                    ctx.rule_type = "Float"
                    ctx.value = ctx.getChild(0).value - ctx.getChild(2).value
                elif left_child_type == "Integer" and right_child_type == "String": #Integer - String
                    ctx.rule_type = "Error"
                    ctx.value = ""
                elif left_child_type == "Float" and right_child_type == "String": #Float - String
                    ctx.rule_type = "Error"
                    ctx.value = ""
                else:
                    ctx.rule_type = "No idea for exitExpr operator == -"
                    ctx.value = "???-"

        # Exit a parse tree produced by ArithmeticExpressionParser#term_mul_op.
    def exitTerm(self, ctx: ArithmeticExpressionParser.TermContext):
        if ctx.getChildCount() == 1:
            ctx.value = ctx.getChild(0).value
            ctx.rule_type = ctx.getChild(0).rule_type
        else:
            operator = ctx.getChild(1).getText()
            if operator == "*":
                left_child_type = ctx.getChild(0).rule_type
                right_child_type = ctx.getChild(2).rule_type
                if left_child_type == "String" and (right_child_type == "String" or right_child_type == "Integer"
                                                    or right_child_type == "Float"): #String * (String or Integer or Float)
                    ctx.rule_type = "Error"
                    ctx.value = ""
                elif left_child_type == "Integer" and right_child_type == "Integer":  # Integer * Integer
                    ctx.rule_type = "Integer"
                    ctx.value = ctx.getChild(0).value * ctx.getChild(2).value
                elif left_child_type == "Integer" and right_child_type == "Float": #Integer * Float
                    ctx.rule_type = "Float"
                    ctx.value = ctx.getChild(0).value * ctx.getChild(2).value
                elif left_child_type == "Float" and right_child_type == "Integer": #Float * Integer
                    ctx.rule_type = "Float"
                    ctx.value = ctx.getChild(0).value * ctx.getChild(2).value
                elif left_child_type == "Float" and right_child_type == "Float": #Float * Float
                    ctx.rule_type = "Float"
                    ctx.value = ctx.getChild(0).value * ctx.getChild(2).value
                elif left_child_type == "Integer" and right_child_type == "String": #Integer * String
                    ctx.rule_type = "Error"
                    ctx.value = ""
                elif left_child_type == "Float" and right_child_type == "String": #Float * String
                    ctx.rule_type = "Error"
                    ctx.value = ""
                else:
                    ctx.rule_type = "No idea for exitExpr operator == *"
                    ctx.value = "???*"
            if operator == "/":
                left_child_type = ctx.getChild(0).rule_type
                right_child_type = ctx.getChild(2).rule_type
                if left_child_type == "String" and (right_child_type == "String" or right_child_type == "Integer"
                                                    or right_child_type == "Float"): #String / (String or Integer or Float)
                    ctx.rule_type = "Error"
                    ctx.value = ""
                elif left_child_type == "Integer" and right_child_type == "Integer":  # Integer / Integer
                    ctx.rule_type = "Float"
                    ctx.value = ctx.getChild(0).value / ctx.getChild(2).value
                elif left_child_type == "Integer" and right_child_type == "Float": #Integer / Float
                    ctx.rule_type = "Float"
                    ctx.value = ctx.getChild(0).value / ctx.getChild(2).value
                elif left_child_type == "Float" and right_child_type == "Integer": #Float / Integer
                    ctx.rule_type = "Float"
                    ctx.value = ctx.getChild(0).value / ctx.getChild(2).value
                elif left_child_type == "Float" and right_child_type == "Float": #Float / Float
                    ctx.rule_type = "Float"
                    ctx.value = ctx.getChild(0).value / ctx.getChild(2).value
                elif left_child_type == "Integer" and right_child_type == "String": #Integer / String
                    ctx.rule_type = "Error"
                    ctx.value = ""
                elif left_child_type == "Float" and right_child_type == "String": #Float / String
                    ctx.rule_type = "Error"
                    ctx.value = ""
                else:
                    ctx.rule_type = "No idea for exitExpr operator == /"
                    ctx.value = "???/"

    # Exit a parse tree produced by ArithmeticExpressionParser#factor_is_numeric.
    def exitFactor_is_integer(self, ctx:ArithmeticExpressionParser.Factor_is_integerContext):
        ctx.rule_type = "Integer"
        if ctx.getChildCount() == 1:
            ctx.value = int(ctx.getText())
        else:
            if ctx.getChild(0).getText() == '+':
                ctx.value = int(ctx.getChild(1).getText())
            if ctx.getChild(0).getText() == '-':
                ctx.value = -1 * int(ctx.getChild(1).getText())

    def exitFactor_is_float(self, ctx:ArithmeticExpressionParser.Factor_is_floatContext):
        ctx.rule_type = "Float"
        if ctx.getChildCount() == 1:
            ctx.value = float(ctx.getText())
        else:
            if ctx.getChild(0).getText() == '+':
                ctx.value = float(ctx.getChild(1).getText())
            if ctx.getChild(0).getText() == '-':
                ctx.value = -1 * float(ctx.getChild(1).getText())

    # Exit a parse tree produced by ArithmeticExpressionParser#factor_is_expression.
    def exitFactor_is_expression(self, ctx:ArithmeticExpressionParser.Factor_is_expressionContext):
        ctx.value = ctx.getChild(1).value
        ctx.rule_type = "Integer"

    # Exit a parse tree produced by ArithmeticExpressionParser#factor_is_id.
    def exitFactor_is_id(self, ctx:ArithmeticExpressionParser.Factor_is_idContext):
        ctx.value = ctx.getText()
        ctx.rule_type = "Identifier"

    # Exit a parse tree produced by ArithmeticExpressionParser#factor_is_string.
    def exitFactor_is_string(self, ctx:ArithmeticExpressionParser.Factor_is_stringContext):
        ctx.rule_type = "String"
        ctx.value = ctx.getText()
