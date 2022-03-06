from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {"(": ")", "{": "}", "[": "]"}
        stack = deque()

        for bracket in s:
            if bracket in bracket_map:
                closing_bracket = bracket_map[bracket]
                stack.append(closing_bracket)
            elif not stack or stack.pop() != bracket:
                return False

        return len(stack) == 0


def test_valid_paren():
    assert Solution().isValid('')
    assert Solution().isValid('()')
    assert Solution().isValid("()[]{}")
    assert Solution().isValid("{[]}")


def test_invalid_paren():
    assert not Solution().isValid('(')
    assert not Solution().isValid('())')
    assert not Solution().isValid('()(')
    assert not Solution().isValid("(]")
    assert not Solution().isValid("([)]")


if __name__ == '__main__':
    test_invalid_paren()
