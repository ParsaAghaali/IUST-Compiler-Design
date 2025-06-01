from default_codes.ast import AST
from default_codes.make_ast_subtree import make_ast_subtree
from gen.ExampleDSLListener import ExampleDSLListener

class CustomExampleDSLListener(ExampleDSLListener):
    def __init__(self, rule_names):
        self.overridden_rules = ['program', 'initiate_game', 'output', 'showhint']
        self.rule_names = rule_names
        self.ast = AST()
        self.hint_option = "False"  # Default value

    def exitEveryRule(self, ctx):
        rule_name = self.rule_names[ctx.getRuleIndex()]
        if rule_name not in self.overridden_rules:
            make_ast_subtree(self.ast, ctx, rule_name)

    def exitProgram(self, ctx):
        make_ast_subtree(self.ast, ctx, "program", keep_node=True)

    def exitInitiate_game(self, ctx):
        make_ast_subtree(self.ast, ctx, "initiate_game", keep_node=True)

    def exitBomb_placements(self, ctx):
        ctx.compound = True
        make_ast_subtree(self.ast, ctx, "bomb_placements", keep_node=True)

    def exitOutput(self, ctx):
        make_ast_subtree(self.ast, ctx, "output", keep_node=True)

    def exitShowhint(self, ctx):
        self.hint_option = ctx.option().getText()
        make_ast_subtree(self.ast, ctx, "showhint", keep_node=True)
