from typing import *

class Solution:
    def quick_select(self, nums: List[int], k: int) -> int:
        def partition(left_idx, right_idx):
            pivot = nums[right_idx]
            pivot_idx = left_idx

            for swap_idx in range(left_idx, right_idx):
                if nums[swap_idx] < pivot:
                    nums[swap_idx], nums[pivot_idx] = nums[pivot_idx], nums[swap_idx]
                    pivot_idx += 1
            
            
            nums[right_idx], nums[pivot_idx] = nums[pivot_idx], nums[right_idx]
            return pivot_idx


        def quick_select_rec(left, right, k):
            if left == right: return nums[left]

            pivot_idx = partition(left, right)
            if pivot_idx == k:
                return nums[pivot_idx]
            elif pivot_idx < k:
                return quick_select_rec(pivot_idx + 1, right, k)
            else:
                return quick_select_rec(left, pivot_idx - 1, k)


        return quick_select_rec(0, len(nums) - 1, k - 1)



def test_lower_bound():
    assert Solution().quick_select([8,2,4,3,7], 1) == 2

def test_upper_bound():
    assert Solution().quick_select([8,2,4,3,7], 5) == 8

def test_single_number():
    assert Solution().quick_select([3], 0) == 3

if __name__ == "__main__":
    test_lower_bound()