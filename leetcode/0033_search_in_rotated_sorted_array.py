from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right - 1:
            mid = left + (right - left) // 2
            # found
            if nums[mid] == target:
                return mid
            # rotation on left
            elif nums[mid] < nums[left]:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid
            # rotation on right
            elif nums[mid] > nums[right]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            # no rotation
            else:
                if target < nums[mid]:
                    right = mid
                else:
                    left = mid
                

        if nums[right] == target: return right
        if nums[left] == target: return left
        return -1


def test_happy_path():
    assert Solution().search([4,5,6,7,0,1,2], 0) == 4

def test_not_found():
    assert Solution().search([4,5,6,7,1,2], 0) == -1

def test_two_items():
    assert Solution().search([4,0], 4) == 0
    assert Solution().search([4,0], 0) == 1

def test_three_items():
    assert Solution().search([4,0,3], 4) == 0
    assert Solution().search([4,0,3], 0) == 1
    assert Solution().search([4,0,3], 3) == 2

def test_not_rotated_items():
    assert Solution().search([1,3,5], 1) == 0
    assert Solution().search([1,3,5], 3) == 1
    assert Solution().search([1,3,5], 5) == 2

if __name__ == "__main__":
    test_happy_path()