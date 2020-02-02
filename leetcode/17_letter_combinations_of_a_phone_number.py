class Solution:
    def letterCombinations1(self, digits):
        digit_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                     "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        results = []
        def combinations_rec(idx=0, word=""):
            if idx == len(digits):
                results.append(word)
            else:
                for letter in list(digit_map[digits[idx]]):
                    combinations_rec(idx+1, f"{word}{letter}")

        if digits == "":
            return []
        combinations_rec()
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


sol = Solution()
print(sol.letterCombinations1("23"))
print(sol.letterCombinations2("23"))

