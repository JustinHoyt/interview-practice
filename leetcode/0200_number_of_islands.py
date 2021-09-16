from typing import *

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        def mark_island(i, j):
            if (
                0 <= i < len(grid) and
                0 <= j < len(grid[0]) and
                grid[i][j] == '1'
            ):
                grid[i][j] = 0
                for i_offset, j_offset in [[-1,0], [0,-1], [1,0], [0,1]]:
                    mark_island(i + i_offset,j + j_offset)
            

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == '1':
                    mark_island(i, j)
                    num_islands += 1

        return num_islands


def test_happy_path():
    matrix = [
        ['1', '0', '1'],
        ['1', '1', '1'],
        ['0', '0', '0'],
        ['0', '1', '0']
    ]
    assert Solution().numIslands(matrix) == 2


def test_single_island():
    matrix = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    assert Solution().numIslands(matrix) == 1



if __name__ == "__main__":
    test_happy_path()



