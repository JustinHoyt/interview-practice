from typing import *

class Solution:
    def quick_select(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            pivot = nums[(left + right) // 2]
            while left <= right:
                while nums[left] < pivot: left += 1
                while nums[right] > pivot: right -= 1

                if left <= right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
            return left

        def quick_select_rec(left, right, k):
            if left == right: return nums[left]

            pivot_idx = partition(left, right)

            if pivot_idx == k: return nums[k]
            elif pivot_idx > k:
                return quick_select_rec(left, pivot_idx - 1, k)
            else:
                return quick_select_rec(pivot_idx, right, k)

        return quick_select_rec(0, len(nums) - 1, k - 1)



def test_lower_bound():
    assert Solution().quick_select([8,2,4,3,7], 1) == 2

def test_upper_bound():
    assert Solution().quick_select([8,2,4,3,7], 5) == 8

def test_single_number():
    assert Solution().quick_select([3], 0) == 3

if __name__ == "__main__":
    test_happy_path()