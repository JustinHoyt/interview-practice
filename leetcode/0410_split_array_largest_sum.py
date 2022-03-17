from typing import List
from functools import cache
import math

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int | float:

        @cache
        def get_min_sum(idx: int, subarrays_remaining: int) -> int | float:
            if idx == len(nums) - 1:
                return nums[idx]
            if subarrays_remaining == 1:
                return sum(nums[idx:])
            if len(nums) - idx == subarrays_remaining:
                return max(nums[idx:])

            min_sum = math.inf
            current_sum = 0
            for i in range(idx + 1, len(nums) - subarrays_remaining + 2):
                current_sum += nums[i]

                max_neighbor_array_len = max(current_sum, get_min_sum(i, subarrays_remaining-1))

                min_sum = min(
                    max_neighbor_array_len,
                    min_sum,
                )

            return min_sum

        return get_min_sum(0, m)


def test_happy_path():
    assert Solution().splitArray([7,2,5,10,8], 2) == 18
    assert Solution().splitArray([1,2,3,4,5], 2) == 9


def test_sparse_lists():
    assert Solution().splitArray([1,4,4], 3) == 4


def test_single_num():
    assert Solution().splitArray([1], 1) == 1


def test_tricky():
    assert Solution().splitArray([2,3,1,2,4,3], 5) == 4


def test_new():
    assert Solution().splitArray([2,16,14,15], 2) == 29


if __name__ == "__main__":
    test_new()

