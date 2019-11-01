from typing import List


class Solution:
    def explore_island(self, matrix, visited, i, j):
        if (i >= 0 and
                j >= 0 and
                i < len(matrix) and
                j < len(matrix[i]) and
                matrix[i][j] == 1 and
                (i, j) not in visited):

            visited[(i, j)] = 1
            self.explore_island(matrix, visited, i - 1, j)
            self.explore_island(matrix, visited, i + 1, j)
            self.explore_island(matrix, visited, i, j + 1)
            self.explore_island(matrix, visited, i, j - 1)

    def numIslands2(self, matrix) -> int:
        if len(matrix) == 0:
            return 0
        visited = {}
        num_islands = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1 and (i, j) not in visited:
                    self.explore_island(matrix, visited, i, j)
                    num_islands += 1

        return num_islands


sol = Solution()
matrix = [
    [1, 0, 1],
    [1, 1, 1],
    [0, 0, 0],
    [0, 1, 0]
]
print(sol.numIslands2(matrix))
