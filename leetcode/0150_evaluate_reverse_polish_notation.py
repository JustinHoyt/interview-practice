from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) < 2:
            return -1

        stack = deque()

        result = int(tokens[0])

        for i range(1, len(tokens)):
            if token.isnumeric():
                stack.append(token)
            else:




def test_happy_path():
    assert Solution().evalRPN(["2","1","+","3","*"]) == 9


if __name__ == "__main__":
    test_happy_path()

