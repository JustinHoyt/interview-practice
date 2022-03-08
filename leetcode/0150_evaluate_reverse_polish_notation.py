from collections import deque
from operator import mul, add, sub
from typing import Callable, List
from math import trunc

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        token_to_operator = {
            '*': mul,
            '+': add,
            '-': sub,
            '/': lambda a, b: trunc(a / b)
        }
        flip = lambda fn: lambda *args: fn(*reversed(args))
        stack = deque()

        for i, token in enumerate(tokens):
            if token.lstrip('-').isnumeric():
                stack.append(int(token))
            else:
                op = token_to_operator[token]
                stack.append(flip(op)(stack.pop(), stack.pop()))

        return stack.pop()


def test_happy_path():
    assert Solution().evalRPN(["2","1","+","3","*"]) == 9


def test_div():
    assert Solution().evalRPN(["4","13","5","/","+"]) == 6


def test_complex_case():
    assert Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22


def test_single_token():
    assert Solution().evalRPN(["4"]) == 4


if __name__ == "__main__":
    test_complex_case()

