class Solution:
    def is_match_rec(self, s, p, s_idx, p_idx, memo) -> bool:
        pass

    def is_match(self, s, p) -> bool:
        s_idx, p_idx = 0, 0
        memo = {}


SOL = Solution()
print(SOL.is_match("abbbc", "a*a*b*.c"))
