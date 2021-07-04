from typing import List

class Solution:

    def change1(self, amount: int, coins: List[int]) -> int:
        if not coins:
            if amount == 0:
                return 1
            return 0
        
        coins.sort()
        memo = {}

        def num_ways(amount_left, coin_idx=0):
            key = (amount_left, coin_idx)
            if key in memo:
                return memo[key]
            
            if amount_left == 0:
                return 1
            
            count = 0
            for i in range(coin_idx, len(coins)):
                if amount_left - coins[i] < 0:
                    break
                count += num_ways(amount_left - coins[i], i)
            
            memo[key] = count
            return count

        return num_ways(amount)


    def change2(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]


sol = Solution()
print(sol.change1(5, [1,2,5]))
print(sol.change2(5, [1,2,5]))
