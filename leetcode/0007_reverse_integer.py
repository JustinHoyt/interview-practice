from typing import *
from math import ceil, log10

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        is_negative = True if x < 0 else False
        if is_negative: x *= -1
        num_digits = ceil(log10(x + 1))
        for i in range(num_digits):
            digit = (x // 10**i) % 10
            result += digit * 10**(num_digits - i - 1)

        if is_negative: result *= -1

        return result if (-2**31 <= result < 2**31) else 0

def test_happy_path():
    assert Solution().reverse(123) == 321

def test_negative_int():
    assert Solution().reverse(-123) == -321

def test_no_leading_zeros():
    assert Solution().reverse(120) == 21

def test_100():
    assert Solution().reverse(100) == 1

def test_99():
    assert Solution().reverse(99) == 99

def test_single_digit():
    assert Solution().reverse(3) == 3

def test_0():
    assert Solution().reverse(0) == 0

def test_out_of_32_bit_int_bounds():
    assert Solution().reverse(1534236469) == 0
    assert Solution().reverse(-2147483648) == 0


if __name__ == "__main__":
    test_happy_path()