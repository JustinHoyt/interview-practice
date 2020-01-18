def generateParenthesis(num_pairs):
    ans = []

    def backtrack(parens_string = '', left_count = 0, right_count = 0):
        if len(parens_string) == 2 * num_pairs:
            ans.append(parens_string)
            return

        if left_count < num_pairs:
            backtrack(parens_string + '(', left_count + 1, right_count)

        if right_count < left_count:
            backtrack(parens_string + ')', left_count, right_count + 1)

    backtrack()
    return ans


print(generateParenthesis(3))
