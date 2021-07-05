from collections import defaultdict
from typing import *

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def get_palindrome_length(left_idx: int, right_idx: int) -> str:
            while left_idx-1 >= 0 and right_idx+1 < len(s) and s[left_idx-1] == s[right_idx+1]:
                left_idx -= 1
                right_idx += 1
            return s[left_idx:right_idx+1]

        def get_even_palindrome_length(left_idx: int, right_idx: int) -> str:
            if right_idx < len(s) and s[left_idx] == s[right_idx]:
                return get_palindrome_length(left_idx, right_idx)
            return s[left_idx]

        max_length_str = ''
        for i, letter in enumerate(s):
            odd_palindrome = get_palindrome_length(i, i)
            even_palindrome = get_even_palindrome_length(i, i+1)

            temp_max_str = odd_palindrome if len(odd_palindrome) > len(even_palindrome) else even_palindrome
            max_length_str = max_length_str if len(max_length_str) > len(temp_max_str) else temp_max_str

        return max_length_str


def test_simple_palindrome():
    assert Solution().longestPalindrome('lol') == "lol"

def test_odd_palindrome():
    assert Solution().longestPalindrome('hlolllo') == "olllo"

def test_even_palindrome():
    assert Solution().longestPalindrome('hlollo') == "ollo"

def test_empty_string():
    assert Solution().longestPalindrome('') == ""