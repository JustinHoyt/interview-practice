from typing import List


class Solution:
    def numIslands(self, matrix) -> int:
        if len(matrix) == 0:
            return 0
        visited = {}
        num_islands = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def explore_island(i, j):
            if (0 <= i < len(matrix) and
                    0 <= j < len(matrix[i]) and
                    matrix[i][j] == 1 and
                    (i, j) not in visited):
                visited[(i, j)] = 1
                for i_offset, j_offset in directions:
                    explore_island(i + i_offset, j + j_offset)

        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell == 1 and (i, j) not in visited:
                    explore_island(i, j)
                    num_islands += 1

        return num_islands


sol = Solution()
matrix = [
    [1, 0, 1],
    [1, 1, 1],
    [0, 0, 0],
    [0, 1, 0]
]
print(sol.numIslands(matrix))
