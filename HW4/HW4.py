def eliminate_left_recursion(rules):
    new_rules = {}
    for lhs, rhs_list in rules.items():
        direct_recursion = []
        non_recursion = []
        for rhs in rhs_list:
            if rhs.startswith(lhs):
                direct_recursion.append(rhs[len(lhs):].strip())
            else:
                non_recursion.append(rhs)

        if direct_recursion:
            new_lhs = lhs + "'"
            new_rules[lhs] = [rhs + ' ' + new_lhs for rhs in non_recursion] if non_recursion else ['ε']
            new_rules[new_lhs] = [(rhs + ' ' + new_lhs).strip() for rhs in direct_recursion] + ['ε']
        else:
            new_rules[lhs] = rhs_list

    return new_rules

def left_factor(rules):
    new_rules = {}
    for lhs, alternatives in rules.items():
        if len(alternatives) > 1:
            common_prefix = None
            for alt in alternatives:
                parts = alt.split()
                if common_prefix is None:
                    common_prefix = parts[0]
                elif parts[0] != common_prefix:
                    common_prefix = None
                    break
            if common_prefix:
                new_lhs = lhs + "'"
                new_rules[lhs] = [common_prefix + ' ' + new_lhs]
                new_rules[new_lhs] = [alt[len(common_prefix):].strip() or 'ε' for alt in alternatives]
            else:
                new_rules[lhs] = alternatives
        else:
            new_rules[lhs] = alternatives

    return new_rules
def find_nullable_nonterminals(rules):
    nullable = set()
    changes = True
    while changes:
        changes = False
        for lhs, rhs_list in rules.items():
            for rhs in rhs_list:
                parts = rhs.split()
                if all(part in nullable or part == 'ε' for part in parts):
                    if lhs not in nullable:
                        nullable.add(lhs)
                        changes = True
    return nullable

def remove_null_productions(rules, nullable):
    new_rules = {}
    for lhs, rhs_list in rules.items():
        new_set = set(rhs_list)  
        if lhs in nullable:
            new_set.add('ε')
        for rhs in rhs_list:
            parts = rhs.split()
            for i in range(len(parts)):
                if parts[i] in nullable:
                    new_rhs = parts[:i] + parts[i+1:]
                    if new_rhs:
                        new_set.add(' '.join(new_rhs).strip())
                    else:
                        new_set.add('ε')
        new_rules[lhs] = list(new_set)
    return new_rules
def convert_to_ll1(grammar):
    nullable = find_nullable_nonterminals(grammar)
    grammar = remove_null_productions(grammar, nullable)
    grammar = eliminate_left_recursion(grammar)
    grammar = left_factor(grammar)
    return grammar

grammar = { 
    "E": ["T", "E + T"],
    "F": ["( E )", "id"],
    "T": ["F", "T * F"]
}

ll1_grammar = convert_to_ll1(grammar)
for lhs, rhs_list in ll1_grammar.items():
    print(f"{lhs} -> {' | '.join(rhs_list)}")

#example grammars
# {
#     "E": ["T", "E + T"],
#     "F": ["( E )", "id"],
#     "T": ["F", "T * F"]
# }
