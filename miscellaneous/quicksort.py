from typing import *

class Solution:
    def quicksort(self, nums: List[int]) -> List[int]:
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

        def quicksort_rec(left, right):
            if left >= right: return

            pivot_idx = partition(left, right)

            quicksort_rec(left, pivot_idx - 1)
            quicksort_rec(pivot_idx, right)

        quicksort_rec(0, len(nums) - 1)
        return nums



def test_happy_path():
    assert Solution().quicksort([8,2,4,3,7]) == [2,3,4,7,8]

def test_single_number():
    assert Solution().quicksort([3]) == [3]

def test_empty_list():
    assert Solution().quicksort([]) == []

if __name__ == "__main__":
    test_happy_path()