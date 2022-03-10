from typing import List
from operator import eq, ne


def binary_search(matrix, search_low_bound, low_idx=0, high_idx=None, search_horizontal=True):
    if high_idx is None:
        high_idx = len(matrix[0]) if search_horizontal else len(matrix)

    comparator = ne if search_low_bound else eq

    while low_idx < high_idx:
        mid_idx = (high_idx + low_idx) // 2
        max_in_line = max([row[mid_idx] for row in matrix]) if search_horizontal else max(matrix[mid_idx])
        if comparator(max_in_line, '1'):
            low_idx = mid_idx + 1
        else:
            high_idx = mid_idx

    return low_idx if search_low_bound else low_idx - 1


class Solution:
    def minArea(self, image: List[List[str]], row: int, col: int) -> int:
        left_bound = binary_search(image, search_low_bound=True, high_idx=col, search_horizontal=True)
        right_bound = binary_search(image, search_low_bound=False, low_idx=col, search_horizontal=True)
        top_bound = binary_search(image, search_low_bound=True, high_idx=row, search_horizontal=False)
        bottom_bound = binary_search(image, search_low_bound=False, low_idx=row, search_horizontal=False)

        return (right_bound - left_bound + 1) * (bottom_bound - top_bound + 1)


def test_happy_path():
    assert Solution().minArea([
        ["0","0","1","0"],
        ["0","1","1","0"],
        ["0","1","0","0"]
    ], 0, 2) == 6

    assert Solution().minArea([
        ["1"]
    ], 0, 0) == 1


def test_binary_search_horizontal():
    assert binary_search([
        ["0","0","1","0"],
        ["0","1","1","0"],
        ["0","1","0","0"]
    ], search_low_bound=True, high_idx=2, search_horizontal=True) == 1

    assert binary_search([
        ["0","0","1","0"],
        ["0","1","1","0"],
        ["0","1","0","0"]
    ], search_low_bound=False, low_idx=1, search_horizontal=True) == 2

    assert binary_search([
        ["0","0","1","0"],
        ["0","1","1","0"],
        ["0","1","0","0"]
    ], search_low_bound=True, high_idx=1, search_horizontal=False) == 0

    assert binary_search([
        ["0","0","1","0"],
        ["0","1","1","0"],
        ["0","1","0","0"]
    ], search_low_bound=False, low_idx=1, search_horizontal=False) == 2


if __name__ == "__main__":
    test_binary_search_horizontal()

