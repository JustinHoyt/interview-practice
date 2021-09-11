from typing import *

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_to_chars = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        results = []

        def generatePerm(idx=0, so_far=''):
            if idx == len(digits): 
                results.append(so_far)
                return
            
            for char in digits_to_chars[digits[idx]]:
                generatePerm(idx + 1, so_far + char)

        if len(digits) > 0:
            generatePerm()
        return results

    def letterCombinations2(self, digits):
        digit_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                     "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def combinations_rec(idx=0):
            result = []
            if idx == len(digits):
                return ['']

            for letter in list(digit_map[digits[idx]]):
                for combination in combinations_rec(idx+1):
                    result.append(f"{letter}{combination}")

            return result

        if digits == "":
            return []
        return combinations_rec()


def test_happy_path():
    assert Solution().letterCombinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    assert Solution().letterCombinations2("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]

def test_empty_case():
    assert Solution().letterCombinations("") == []
    assert Solution().letterCombinations2("") == []


if __name__ == "__main__":
    test_happy_path()