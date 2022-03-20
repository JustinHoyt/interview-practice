from itertools import starmap


class Solution:
    def maximalSquare(self, matrix):
        memo = {}
        best = 0

        def _maximal_square(i=0, j=0):
            nonlocal best
            if i == len(matrix) or j == len(matrix[i]):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            lowest_neighbor = min(starmap(_maximal_square, [(i+1, j), (i, j+1), (i+1, j+1)]))

            curr = 0
            if matrix[i][j] == '1':
                curr = 1 + lowest_neighbor

            best = max(curr, best)
            memo[(i, j)] = curr
            return curr

        _maximal_square()
        return best ** 2

matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "1", "1", "1"]
]

sol = Solution()
print(sol.maximalSquare(matrix))
