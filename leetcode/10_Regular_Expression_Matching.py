from typing import Dict


class Solution:
    def is_match_rec(self, string: str, pattern: str, string_idx: int,
                     pattern_idx: int, memo: Dict) -> bool:
        self.print_current_state(string, pattern, string_idx, pattern_idx)
        key = (string_idx, pattern_idx)
        if key in memo:
            return memo[key]
        is_zero_or_many = pattern_idx + 1 < len(pattern) and pattern[pattern_idx + 1] == "*"
        if string_idx >= len(string) and pattern_idx >= len(pattern):
            return True
        if string_idx >= len(string) and pattern_idx == len(pattern) - 2 and is_zero_or_many:
            return True
        if (string_idx >= len(string) or pattern_idx >= len(pattern)) and not is_zero_or_many:
            return False

        if is_zero_or_many:
            # evaluate pattern index, and move string idx
            is_successful_eval = False
            if string_idx < len(string):
                is_successful_eval = ((string[string_idx] == pattern[pattern_idx] or pattern[pattern_idx] == ".")
                                      and self.is_match_rec(string, pattern, string_idx + 1, pattern_idx, memo))
            # do not evaluate pattern index and move on
            is_successful_no_eval = self.is_match_rec(string, pattern, string_idx,
                                                      pattern_idx + 2, memo)
            memo[key] = is_successful_eval or is_successful_no_eval
            return is_successful_eval or is_successful_no_eval

        if pattern[pattern_idx] == string[string_idx] or pattern[pattern_idx] == ".":
            memo[key] = self.is_match_rec(string, pattern, string_idx + 1, pattern_idx + 1, memo)
            return memo[key]

        memo[key] = False
        return False


    def isMatch(self, string, pattern) -> bool:
        string_idx, pattern_idx = 0, 0
        memo = {}
        return self.is_match_rec(string, pattern, string_idx, pattern_idx, memo)

    def print_current_state(self, string, pattern, string_idx, pattern_idx):
        for _ in range(pattern_idx):
            print(" ", end="")
        print("V")
        print(pattern)
        for _ in range(string_idx):
            print(" ", end="")
        print("V")
        print(string)
        print("pattern_idx", pattern_idx)
        print("string_idx", string_idx)
        input()


SOL = Solution()
print("these should be true")
print(SOL.isMatch("abbbc", "a*b*c"))
print(SOL.isMatch("abbbc", "a*a*b*c*"))
print(SOL.isMatch("a", ".*"))
print(SOL.isMatch("a", "a*"))
print(SOL.isMatch("aa", "a*"))
print(SOL.isMatch("aa", "a*."))
print(SOL.isMatch("aa", "a.*c*"))
print(SOL.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*b"))
print()
print("these should be false")
print(SOL.isMatch("aa", "a*c"))
