from typing import *
from math import ceil, log10

class Solution:
    def myAtoi(self, s: str) -> int:
        result_str = ''
        i = 0

        # trim whitespace and leading zeros
        while i < len(s):
            if s[i] != ' ' and s[i] != 0:
                break
            i += 1

        if i >= len(s): return 0
        sign = '+'
        if s[i] in ['-', '+']:
            sign = s[i]
            i += 1

        while i < len(s):
            if not s[i].isdigit(): break

            result_str += s[i]
            i += 1

        if not result_str.isdigit(): return 0

        result_int = int(result_str)
        if sign == '-': result_int *= -1

        if result_int < -2**31: return -2**31
        if result_int >= 2**31: return 2**31-1
        return result_int

def test_happy_path():
    assert Solution().myAtoi('42') == 42

def test_leading_spaces():
    assert Solution().myAtoi('    42') == 42

def test_leading_zeros():
    assert Solution().myAtoi('000042') == 42

def test_positive():
    assert Solution().myAtoi('+42') == 42

def test_negative():
    assert Solution().myAtoi('-42') == -42

def test_negative_invalid():
    assert Solution().myAtoi('-') == 0

def test_bad_input():
    assert Solution().myAtoi('bad input') == 0

def test_empty():
    assert Solution().myAtoi('') == 0

def test_trailing_letters():
    assert Solution().myAtoi('42hello') == 42

def test_out_of_positive_bounds():
    assert Solution().myAtoi('999999999999999999999') == 2**31 - 1

def test_out_of_positive_bounds():
    assert Solution().myAtoi('-999999999999999999999') == -2**31

if __name__ == "__main__":
    test_positive()