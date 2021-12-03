from typing import List
import math

class Solution:
    def coinChange(self, coins, amount):
        memo = {}
        coins.sort()
        coins.reverse()

        def coin_change_rec(so_far, coins_so_far):
            key = so_far
            if key in memo: return memo[key]

            if so_far == amount:
                memo[key] = 1
                return memo[key]
            elif so_far < amount:
                temp_coins = math.inf
                for coin in coins:
                    temp_coins = min(temp_coins, coin_change_rec(so_far + coin, coins_so_far + 1))
                return temp_coins + 1
            else:
                return math.inf

        if amount == 0: return 0
        result = coin_change_rec(0, 0)
        return -1 if result == math.inf else result


def test_zero():
    assert Solution().coinChange([1,2,5], 0) == 0

def test_no_result():
    assert Solution().coinChange([2,5], 3) == -1

def test_happy_path():
    assert Solution().coinChange([1,2,5], 100) == 3

if __name__ == "__main__":
    test_happy_path()
