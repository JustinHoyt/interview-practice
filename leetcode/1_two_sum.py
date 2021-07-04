from collections import defaultdict
from functools import partial
from typing import *

'''
Constraints:
1. Exactly one solution
2. You may not use the same element twice
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map: Dict[List[int], List[int]] = defaultdict(list)
        for i, num in enumerate(nums):
            nums_map[num].append(i)

        for num_idx, num in enumerate(nums):
            remainder = target - num
            if remainder in nums_map:
                for remainder_idx in nums_map[remainder]:
                    if num_idx != remainder_idx:
                        return [num_idx, remainder_idx]
        return False


def test_two_positive_ints():
    assert Solution().twoSum([1,2,3], 5) == [1,2]

def test_two_negative_ints():
    assert Solution().twoSum([1,-2,-3], -5) == [1,2]

def test_one_negative_int():
    assert Solution().twoSum([-1,5,3], 2) == [0,2]

def test_cannot_use_same_element():
    assert Solution().twoSum([-1,5,3,7], 10) == [2,3]