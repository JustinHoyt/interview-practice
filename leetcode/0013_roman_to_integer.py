from typing import *

class Solution:
    def romanToInt(self, roman: str) -> int:
        def should_subtract(idx):
            return i + 1 < len(roman) and roman_to_int[roman[idx]] < roman_to_int[roman[idx+1]]

        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        result = 0
        for i, char in enumerate(roman):
            result = result - roman_to_int[char] if should_subtract(i) else result + roman_to_int[char]
        return result



def test_happy_path():
    assert Solution().romanToInt('III') == 3

def test_subtraction():
    assert Solution().romanToInt('IV') == 4

def test_higher_characters():
    assert Solution().romanToInt('LVIII') == 58

def test_multiple_subtraction():
    assert Solution().romanToInt('MCMXCIV') == 1994

if __name__ == "__main__":
    test_happy_path()