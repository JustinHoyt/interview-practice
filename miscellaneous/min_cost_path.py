def min_cost_path_rec(grid, i, j):
    if i == len(grid) or j == len(grid[0]):
        return float('inf')
    if i == len(grid) - 1 and j == len(grid[0]) - 1:
        return grid[-1][-1]
    lowest_path = min(min_cost_path_rec(grid, i+1, j), min_cost_path_rec(grid, i, j+1))
    return lowest_path + grid[i][j]


def min_cost_path(grid):
    i = 0
    j = 0
    return min_cost_path_rec(grid, i, j)


grid = [
    [1,3,1],
    [1,5,1],
    [4,2,1],
]

print(min_cost_path(grid))
