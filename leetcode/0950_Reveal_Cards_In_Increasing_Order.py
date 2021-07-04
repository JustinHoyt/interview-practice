from collections import deque

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        d = deque()
        for card in sorted(deck, reverse=True):
            d.rotate()
            d.appendleft(card)
        return list(d)

sol = Solution()
print(sol.deckRevealedIncreasing([17,13,11,2,3,5,7]))