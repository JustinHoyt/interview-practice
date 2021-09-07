from typing import *
from math import log10, ceil

class Solution:
    def isPalindrome(self, num: int) -> bool:
        def int_len(num):
            return ceil(log10(num + 1))

        def get_digit(idx):
            return (num // 10**idx) % 10

        if num < 0: return False

        small_digit_idx = 0
        large_digit_idx = int_len(num) - 1
        while small_digit_idx < large_digit_idx:
            if get_digit(small_digit_idx) != get_digit(large_digit_idx):
                return False
            small_digit_idx += 1
            large_digit_idx -= 1
        
        return True


def test_palindrome_number():
    assert Solution().isPalindrome(121) == True

def test_negative_palindrome_should_be_false():
    assert Solution().isPalindrome(-121) == False

def test_non_palindrome():
    assert Solution().isPalindrome(10) == False

def test_single_digit_is_palindrome():
    assert Solution().isPalindrome(1) == True

def test_long_non_palindrome():
    assert Solution().isPalindrome(1000021) == False

if __name__ == "__main__":
    test_long_non_palindrome()