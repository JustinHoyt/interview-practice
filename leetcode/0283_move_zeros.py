from typing import *

class Solution:
    """
    Do not return anything, modify nums in-place instead.
    """
    def moveZeroes(self, nums: List[int]) -> None:
        swap_idx = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[swap_idx], nums[i] = nums[i], nums[swap_idx]
                swap_idx += 1


def test_happy_path():
    actual = [0,1,0,3,12]
    Solution().moveZeroes(actual) 
    assert actual == [1,3,12,0,0]


if __name__ == "__main__":
    test_happy_path()