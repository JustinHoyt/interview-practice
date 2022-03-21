from timer import timer
from math import inf
from functools import cache
from itertools import starmap
from collections import deque

class Solution:
    @timer
    def shortestPathBFS(self, grid: list[list[int]], num_unblocks: int) -> float:
        num_rows, num_cols = len(grid), len(grid[0])
        state = (0, 0, num_unblocks)
        queue: deque[tuple[int, tuple[int, int, int]]] = deque([(0, state)])
        visited: set[tuple[int, int, int]] = set()

        if num_unblocks >= num_rows + num_cols - 2:
            return num_rows + num_cols - 2

        while queue:
            steps, (i, j, num_unblocks) = queue.popleft()

            if (i, j) == (num_rows - 1, num_cols - 1):
                return steps

            if not (0 <= i < num_rows and 0 <= j < num_cols):
                continue

            num_unblocks = num_unblocks - grid[i][j]

            state = (i, j, num_unblocks)

            if num_unblocks < 0 or state in visited:
                continue

            visited.add(state)
            for _i, _j in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                queue.append((steps+1, (_i, _j, num_unblocks)))

        return -1


    @timer
    def shortestPathDFS(self, grid: list[list[int]], num_unblocks: int) -> float:
        visited: set[tuple[int, int, int]] = set()

        @cache
        def shortest_path(i=0, j=0, _k=num_unblocks) -> float:
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

            return min(starmap(shortest_path, [(i+1, j, _k), (i, j+1, _k), (i-1, j, _k), (i, j-1, _k)])) + 1

        min_path = shortest_path()
        return min_path if min_path != inf else -1


def test_happy_path():
    obj = Solution()
    for func in [obj.shortestPathBFS, obj.shortestPathDFS]:
        assert func([
            [0,0,0],
            [1,1,0],
            [0,0,0],
            [0,1,1],
            [0,0,0]
        ], 1) == 6


def test_viable_blocked_path():
    obj = Solution()
    for func in [obj.shortestPathBFS, obj.shortestPathDFS]:
        assert func([
            [0,0,0],
            [1,1,0],
            [0,0,0],
            [1,1,1],
            [0,0,0]
        ], 1) == 6


def test_no_path():
    obj = Solution()
    for func in [obj.shortestPathBFS, obj.shortestPathDFS]:
        assert func([
            [0,0,0],
            [1,1,0],
            [1,1,1],
            [1,1,1],
            [0,0,0]
        ], 1) == -1


def test_k_greater_than_number_of_obstacles():
    obj = Solution()
    for func in [obj.shortestPathBFS, obj.shortestPathDFS]:
        assert func([
            [0,1,0,1],
            [0,1,0,0],
            [0,0,1,0],
            [1,0,0,1],
            [0,1,0,0]
        ], 18) == 7


if __name__ == "__main__":
    test_happy_path()

