import math as m
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def change(amount_left):
            if amount_left == 0:
                return 0
            if amount_left <= 0:
                return m.inf
            fewest_ways = m.inf
            for coin in coins:
                fewest_ways = min(fewest_ways, change(amount_left - coin) + 1)

            return fewest_ways

        result = change(amount)
        if result == m.inf:
            return -1
        return result

print(Solution().coinChange([1,2,5], 11))