from typing import *
import math

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2: return False
        sum = nums[0]
        remainders: Set[int] = set()
        remainders.add(0)

        prev_remainder = nums[0] % k
        for i in range(1, len(nums)):
            sum += nums[i]
            remainder = sum % k
            if remainder in remainders: 
                return True
            
            remainders.add(prev_remainder)
            prev_remainder = remainder

        return False


def test_happy_path():
    assert Solution().checkSubarraySum([23,2,4,6,7], 6) == True

def test_single_item():
    assert Solution().checkSubarraySum([5], 5) == False

def test_no_match():
    assert Solution().checkSubarraySum([23,6,9], 13) == False


if __name__ == "__main__":
    test_no_match()