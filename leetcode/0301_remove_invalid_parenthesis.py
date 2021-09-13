from typing import *

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        biggest_size = 0
        results: List[str] = []

        paren_value = {
            '(': 1,
            ')': -1
        }

        def generateParens(sofar: str = '', idx: int = 0, count: int = 0):
            nonlocal results, biggest_size

            if count == 0:
                if len(sofar) == biggest_size and sofar not in results:
                    results.append(sofar)
                elif len(sofar) > biggest_size:
                    results = [sofar]
                    biggest_size = len(sofar)

            # if there are more unclosed parens than remaining chars
            if len(s) - idx < count: return
            if idx == len(s): return
            if count < 0: return
            
            generateParens(sofar, idx+1, count)
            generateParens(sofar + s[idx], idx+1, count + paren_value.get(s[idx], 0))

        generateParens()
        return results



def test_happy_path():
    assert Solution().removeInvalidParentheses("(a)())()") == ["(a())()","(a)()()"]

def test_completely_invalid_string():
    assert Solution().removeInvalidParentheses(")(") == [""]

def test_empty_input():
    assert Solution().removeInvalidParentheses("") == [""]

def test_time_limit():
    assert Solution().removeInvalidParentheses("((((((((((((((((((((aaaaa") == ["aaaaa"]


if __name__ == "__main__":
    test_happy_path()