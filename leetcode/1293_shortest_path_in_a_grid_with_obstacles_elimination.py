from math import inf
from functools import cache, partial
from itertools import starmap

class Solution:
    def shortestPathDFS(self, grid: list[list[int]], k: int) -> int | float:
        visited: set[tuple[int, int, int]] = set()

        @cache
        def shortest_path(i=0, j=0, _k=k) -> int | float:
            if (not (0 <= i < len(grid) and 0 <= j < len(grid[0]))
                    or (i, j, _k) in visited):
                return inf

            if grid[i][j] == 1:
                if _k > 0:
                    _k -= 1
                else:
                    return inf

            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return 0

            visited.add((i, j, _k))

            return min(starmap(partial(shortest_path, _k=_k), [(i+1, j), (i, j+1), (i-1, j), (i, j-1)])) + 1

        min_path = shortest_path()
        return min_path if min_path != inf else -1


def test_happy_path():
    assert Solution().shortestPathDFS([
        [0,0,0],
        [1,1,0],
        [0,0,0],
        [0,1,1],
        [0,0,0]
    ], 1) == 6


def test_viable_blocked_path():
    assert Solution().shortestPathDFS([
        [0,0,0],
        [1,1,0],
        [0,0,0],
        [1,1,1],
        [0,0,0]
    ], 1) == 6


def test_no_path():
    assert Solution().shortestPathDFS([
        [0,0,0],
        [1,1,0],
        [1,1,1],
        [1,1,1],
        [0,0,0]
    ], 1) == -1


def test_k_greater_than_number_of_obstacles():
    assert Solution().shortestPathDFS([
        [0,1,0,1],
        [0,1,0,0],
        [0,0,1,0],
        [1,0,0,1],
        [0,1,0,0]
    ], 18) == 7


if __name__ == "__main__":
    test_k_greater_than_number_of_obstacles()

