class Solution:
    def maximalSquare(self, matrix):
        memo = {}
        best = 0

        def dfs(i, j):
            nonlocal best
            if i == len(matrix) or j == len(matrix[i]):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            lowest_neighbor = min(dfs(i+1, j), dfs(i, j+1), dfs(i+1, j+1))

            curr = 0
            if matrix[i][j] == '1':
                curr = 1 + lowest_neighbor

            best = max(curr, best)
            memo[(i, j)] = curr
            return curr

        dfs(0, 0)
        return best ** 2

matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "1", "1", "1"]
]

sol = Solution()
print(sol.maximalSquare(matrix))
