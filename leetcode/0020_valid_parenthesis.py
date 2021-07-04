from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {"(": ")", "{": "}", "[": "]"}
        stack = deque()

        for bracket in s:
            if bracket in bracket_map:
                closing_bracket = bracket_map[bracket]
                stack.append(closing_bracket)
            elif stack.pop() != bracket:
                return False

        return len(stack) == 0


sol = Solution()
print(sol.isValid("()("))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([)]"))
print(sol.isValid("{[]}"))
