from typing import *
from random import shuffle

class Solution:
    def quicksort(self, nums: List[int]) -> List[int]:
        def partition(left: int, right: int) -> int:
            pivot = nums[right]
            pivot_idx = left
            for swap_idx in range(left, right):
                if nums[swap_idx] < pivot:
                    nums[pivot_idx], nums[swap_idx] = nums[swap_idx], nums[pivot_idx]
                    pivot_idx += 1

            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            return pivot_idx


        def quicksort_rec(left: int, right: int):
            if left >= right: return

            pivot_idx = partition(left, right)

            quicksort_rec(left, pivot_idx - 1)
            quicksort_rec(pivot_idx + 1, right)

        quicksort_rec(0, len(nums) - 1)
        return nums


def test_happy_path():
    assert Solution().quicksort([8,2,4,3,7]) == [2,3,4,7,8]

def test_single_number():
    assert Solution().quicksort([3]) == [3]

def test_empty_list():
    assert Solution().quicksort([]) == []

def test_generate_numbers():
    for i in range(-99, 100):
        random_list = list(range(i))
        shuffle(random_list)
        sorted_list = list(range(i))
        assert Solution().quicksort(random_list) == sorted_list

if __name__ == "__main__":
    test_happy_path()