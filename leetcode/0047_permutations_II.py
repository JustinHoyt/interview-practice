from typing import *

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def permute_rec(idx = 0) -> None:
            if idx == len(nums):
                results.append(nums.copy())

            swaps = set()
            for i in range(idx, len(nums)):
                key = (nums[idx], nums[i])
                if key in swaps: continue
                swaps.add(key)

                swap(idx, i)
                permute_rec(idx + 1)
                swap(idx, i)

        results: List[List[int]] = []

        if len(nums) == 0:
            return []
        permute_rec()
        print(results)
        return results


def test_happy_path():
    assert Solution().permuteUnique([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2]]

def test_with_identical_numbers():
    assert Solution().permuteUnique([1,1,2]) == [[1,1,2], [1,2,1], [2,1,1]]

def test_with_sets_of_identical_numbers():
    assert Solution().permuteUnique([1,1,2,2]) == [[1,1,2,2], [1,2,1,2], [1,2,2,1], [2,1,1,2], [2,1,2,1], [2,2,1,1]]

def test_one_element():
    assert Solution().permuteUnique([1]) == [[1]]

def test_zero_elements():
    assert Solution().permuteUnique([]) == []


if __name__ == "__main__":
    test_with_identical_numbers()