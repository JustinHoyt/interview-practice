from typing import *
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prices = prices.copy()
        max_profit = 0

        for i in range(len(prices) - 2, -1, -1):
            max_prices[i] = max(max_prices[i+1], prices[i])
        
        for i, price in enumerate(prices):
            max_profit = max(max_prices[i] - price, max_profit)
        
        return max_profit


def test_happy_path():
    assert Solution().maxProfit([7,1,5,3,6,4]) == 5

def test_no_profit():
    assert Solution().maxProfit([7,6,5,3,2,1]) == 0

def test_bounds():
    assert Solution().maxProfit([]) == 0
    assert Solution().maxProfit([1]) == 0

if __name__ == "__main__":
    test_happy_path()