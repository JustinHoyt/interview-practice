# from functools import cache

# A simple reimplementation of the @cache decorator for educational purposes
def _cache(fn):
    cache = {}

    def cache_wrapper(*args):
        key = args
        if key not in cache:
            cache[key] = fn(*args)
        return cache[key]

    return cache_wrapper


class Solution:
    def longestIncreasingPath(self, matrix):
        @_cache
        def dfs(i, j):
            max_result = 0
            for _i, _j in [[i,j+1], [i,j-1], [i+1,j], [i-1,j]]:
                if 0 <= _i < len(matrix) and 0 <= _j < len(matrix[0]) and matrix[_i][_j] > matrix[i][j]:
                    max_result = max(dfs(_i, _j) + 1, max_result)

            return max_result


        return max([dfs(i, j) + 1 for i in range(len(matrix)) for j in range(len(matrix[0]))])


def test_happy_path():
    nums = [
      [3,4,5],
      [3,2,6],
      [2,2,1]
    ]
    assert Solution().longestIncreasingPath(nums) == 4

if __name__ == '__main__':
    test_happy_path()
