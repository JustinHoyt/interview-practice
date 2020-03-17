class Solution(object):
    def scoreOfParentheses(self, S):
        stack = [0]

        for paren in S:
            if paren == '(':
                stack.append(0)
            else:
                running_score = stack.pop()
                stack[-1] += max(2 * running_score, 1)

        return stack.pop()


class Solution(object):
    def scoreOfParentheses(self, S):
        score = 0
        depth = 0
        for i, paren in enumerate(S):
            if paren == '(':
                depth += 1
            else:
                depth -= 1
                if S[i-1] == '(':
                    score += 2 ** depth
        return score

sol = Solution()
print(sol.scoreOfParentheses('(()(()))'))

