from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def first_decreasing_idx() -> int:
            for i in range(len(nums) - 1, 0, -1):
                if nums[i - 1] < nums[i]:
                    return i - 1

            return -1


        def find_swap_idx(start_idx: int) -> int:
            for i in range(len(nums) - 1, -1, -1):
                if nums[start_idx] < nums[i]:
                    return i


        def reverse_sublist(left_idx: int) -> None:
            right_idx = len(nums) - 1
            while left_idx < right_idx:
                nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
                left_idx += 1
                right_idx -= 1


        if len(nums) < 2:
            return

        idx = first_decreasing_idx()
        if idx == -1:
            nums.reverse()
            return

        swap_idx = find_swap_idx(idx)

        nums[idx], nums[swap_idx] = nums[swap_idx], nums[idx]

        reverse_sublist(idx + 1)


def test_happy_path():
    nums = [1,2,3]
    Solution().nextPermutation(nums)
    assert nums == [1,3,2]


def test_reverse_case():
    nums = [3,2,1]
    Solution().nextPermutation(nums)
    assert nums == [1,2,3]


def test_middle_case():
    nums = [1,3,5,4,2,1]
    Solution().nextPermutation(nums)
    assert nums == [1,4,1,2,3,5]


def test_single_case():
    nums = [1]
    Solution().nextPermutation(nums)
    assert nums == [1]


def test_zero_case():
    nums = []
    Solution().nextPermutation(nums)
    assert nums == []


if __name__ == "__main__":
    test_reverse_case()

