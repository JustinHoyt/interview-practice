from typing import List
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        memo = {}
        def dfs(i, j, z):
            if i == m-1 and j == n-1:
                return 0

            if i >= m or j >= n or i < 0 or j < 0:
                return -1

            if (i, j, z) in memo:
                return memo[(i, j, z)]

            # we have been there
            if grid[i][j] == -1:
                return -1

            if grid[i][j] == 1:
                if z == 0:
                    return -1
                else:
                    grid[i][j] = 0  # unlock it
                    ans = dfs(i, j, z - 1)
                    grid[i][j] = 1  # restore it

                    memo[(i, j, z)] = ans
                    return ans
            else:
                ans = float('inf')
                grid[i][j] = -1
                for di, dj in dirs:
                    result = dfs(i + di, j + dj, z)
                    if result != -1:
                        ans = min(result + 1, ans)

                grid[i][j] = 0
                if ans == float('inf'):
                    ans = -1

                memo[(i, j, z)] = ans

            return ans

        result = dfs(0, 0, k)
        return result


grid = [[0,0,0],
        [1,1,0],
        [0,0,0],
        [0,1,1],
        [0,0,0]]
k = 1

print(Solution().shortestPath(grid, k))