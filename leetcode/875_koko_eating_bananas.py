from math import ceil
from functools import reduce

class Solution:
    def time_to_eat(self, piles, bananas_per_hour):
        return reduce(lambda acc, pile: acc + ceil(pile / bananas_per_hour), piles, 0)

    def minEatingSpeed(self, piles, H):
        low = 1
        high = max(piles)

        while low <= high:
            bananas_per_hour = (low + high) // 2

            time = self.time_to_eat(piles, bananas_per_hour)

            if time <= H:
                high = bananas_per_hour - 1
            else:
                low = bananas_per_hour + 1

        return low


sol = Solution()
print(sol.minEatingSpeed([3, 6, 7, 11], 8))
print(sol.minEatingSpeed([30, 11, 23, 4, 20], 5))
print(sol.minEatingSpeed([30, 11, 23, 4, 20], 6))
print(sol.minEatingSpeed([332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589, 290818316, 877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184], 823855818))
