from typing import List
from random import randint


class Solution:
    def __init__(self, nums: List[int]):
        self.orig_nums = nums[:]
        self.nums = nums

    def reset(self) -> List[int]:
        self.nums = self.orig_nums[:]
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            swap_idx = randint(i, len(self.nums) - 1)
            self.nums[i], self.nums[swap_idx] = self.nums[swap_idx], self.nums[i]

        return self.nums


def test_happy_path():
    obj = Solution([1,2,3,4,5])

    print(obj.shuffle())
    print(obj.shuffle())
    print(obj.shuffle())
    print(obj.shuffle())
    print(obj.shuffle())
    print(obj.shuffle())
    print(obj.shuffle())
    print(obj.shuffle())
    print(obj.shuffle())
    print(obj.shuffle())
    print(obj.reset())


if __name__ == "__main__":
    test_happy_path()

