class Solution:
    def longestIncreasingPath(self, matrix):
        if len(matrix) == 0:
            return 0

        cache = [[0] * len(matrix[0]) for x in range(len(matrix))]

        ans = 0
        for i, row in enumerate(matrix):
            for j, _ in enumerate(row):
                ans = max(ans, self.dfs(matrix, i, j, cache))
        return ans

    def dfs(self, matrix, i, j, cache):
        if cache[i][j] != 0:
            return cache[i][j]

        for row_shift, col_shift in [(0,1), (1,0), (0, -1), (-1, 0)]:
            next_i = i + row_shift
            next_j = j + col_shift

            if (0 <= next_i < len(matrix)
                    and 0 <= next_j < len(matrix[0])
                    and matrix[next_i][next_j] > matrix[i][j]):
                cache[i][j] = max(cache[i][j], self.dfs(matrix, next_i, next_j, cache))

        return cache[i][j] + 1

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
sol = Solution()
print(sol.longestIncreasingPath(nums))

