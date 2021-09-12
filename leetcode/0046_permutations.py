from typing import *

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def permute_rec(idx = 0) -> None:
            if idx == len(nums):
                results.append(nums.copy())

            for i in range(idx, len(nums)):
                swap(idx, i)
                permute_rec(idx + 1)
                swap(idx, i)

        results: List[List[int]] = []

        if len(nums) == 0:
            return []
        permute_rec()
        return results


def test_happy_path():
    assert Solution().permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2]]

def test_one_element():
    assert Solution().permute([1]) == [[1]]

def test_zero_elements():
    assert Solution().permute([]) == []


if __name__ == "__main__":
    test_happy_path()