from collections import deque

def balanced_brackets(brackets):
    opening_bracket_stack = deque()
    opening_bracket_map = {"{": "}", "[": "]", "(": ")"}
    for bracket in brackets:
        if bracket in opening_bracket_map:
            opening_bracket_stack.append(bracket)
        else:
            is_complementary_brackets = bracket == opening_bracket_map[opening_bracket_stack.pop()]
            if not is_complementary_brackets:
                return False
    return True


brackets1 = '{[()]}'
brackets2 = '{[(])}'
brackets3 = '{{[[(())]]}}'
print(balanced_brackets(brackets1))
print(balanced_brackets(brackets2))
print(balanced_brackets(brackets3))
