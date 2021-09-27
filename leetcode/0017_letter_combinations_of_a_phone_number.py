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
        results: List[str] = []

        def generateCombinations(sofar='', idx=0):
            nonlocal results
            if len(digits) == len(sofar):
                results.append(sofar)
                return

            for letter in digits_to_chars[digits[idx]]:
                generateCombinations(f'{sofar}{letter}', idx+1)
        
        if digits:
            generateCombinations()
        return results
    
    def letterCombinations2(self, digits: str) -> List[str]:
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

        def generateCombinations(idx=0):
            if idx == len(digits):
                return ['']
            
            results = []
            for letter in digits_to_chars[digits[idx]]:
                for combination in generateCombinations(idx + 1):
                    results.append(f'{letter}{combination}')
            
            return results

        return generateCombinations() if digits else []






def test_happy_path():
    assert sorted(Solution().letterCombinations("23")) == sorted(["ad","ae","af","bd","be","bf","cd","ce","cf"])
    assert sorted(Solution().letterCombinations2("23")) == sorted(["ad","ae","af","bd","be","bf","cd","ce","cf"])

def test_empty_case():
    assert Solution().letterCombinations("") == []
    assert Solution().letterCombinations2("") == []


if __name__ == "__main__":
    test_happy_path()