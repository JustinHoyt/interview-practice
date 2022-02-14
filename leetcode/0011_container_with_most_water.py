from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_idx = 0
        right_idx = len(heights) - 1
        max_area = 0

        while left_idx < right_idx:
            lowest_height = min(heights[left_idx], heights[right_idx])
            max_area = max(lowest_height * (right_idx - left_idx), max_area)

            if heights[left_idx] < heights[right_idx]:
                left_idx += 1
            else:
                right_idx -= 1

        return max_area


def test_happy_path():
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


if __name__ == "__main__":
    test_happy_path()
