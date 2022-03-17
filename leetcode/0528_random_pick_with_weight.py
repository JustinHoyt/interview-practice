from random import randint
from bisect import bisect_left

class Solution:
    def __init__(self, weights: list[int]):
        self.weights = weights
        self.sum_weights = []

        for i, weight in enumerate(weights):
            self.sum_weights.append(weight + (self.sum_weights[i-1] if i > 0 else 0))


    def pickIndex(self) -> int:
        target = randint(1, self.sum_weights[-1])
        placement_idx = bisect_left(self.sum_weights, target)
        return placement_idx


def test_happy_path():
    print(Solution([1]).pickIndex())
    print(Solution([1,2,3]).pickIndex())
    print(Solution([1,2,3]).pickIndex())
    print(Solution([1,2,3]).pickIndex())
    print(Solution([1,2,3]).pickIndex())
    print(Solution([1,2,3]).pickIndex())
    print(Solution([1,2,3]).pickIndex())
    print(Solution([1,2,3]).pickIndex())
    print(Solution([1,2,3]).pickIndex())
    print(Solution([1,2,3]).pickIndex())
    print(Solution([1,2,3]).pickIndex())
    print(Solution([1,2,3]).pickIndex())
    print(Solution([1,2,3]).pickIndex())
    print(Solution([1,2,3]).pickIndex())
    print(Solution([1,2,3]).pickIndex())
    print(Solution([1,2,3]).pickIndex())
    print(Solution([1,2,3]).pickIndex())


if __name__ == "__main__":
    test_happy_path()

