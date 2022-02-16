from typing import List
from heapq import heappop, heappush


class Solution:
    def sort_messy_array(self, nums: List[int], distance: int) -> List[int]:
        left_idx = 0
        right_idx = distance
        min_heap = []

        if distance >= len(nums):
            distance = len(nums) - 1

        for i in range(distance + 1):
            heappush(min_heap, nums[i])

        while right_idx < len(nums):
            nums[left_idx] = heappop(min_heap)

            left_idx += 1
            right_idx += 1

            if right_idx < len(nums):
                heappush(min_heap, nums[right_idx])

        while min_heap:
            nums[left_idx] = heappop(min_heap)
            left_idx += 1

        return nums


def test_happy_path():
    assert Solution().sort_messy_array([2, 5, 3, 7, 4], 2) == [2, 3, 4, 5, 7]


def test_single_item():
    assert Solution().sort_messy_array([2], 1) == [2]


def test_empty_list():
    assert Solution().sort_messy_array([], 0) == []


def test_k_greater_than_n():
    assert Solution().sort_messy_array([2, 5, 3, 7, 4], 6) == [2, 3, 4, 5, 7]


if __name__ == "__main__":
    test_happy_path()
