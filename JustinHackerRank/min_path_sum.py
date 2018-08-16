import math

def min_path_sum(grid, memo, i, j):
    if memo[i][j] != -1:
        return memo[i][j]

    if i == len(grid)-1 and j == len(grid[0])-1:
        return grid[i][j]

    down = math.inf
    right = math.inf
    if i+1 < len(grid):
        down = min_path_sum(grid, memo, i+1, j)
    if j < len(grid[0])-1:
        right = min_path_sum(grid, memo, i, j+1)
    result = min(down, right) + grid[i][j]
    memo[i][j] = result
    for row in memo:
        print(row)
    print()
    return result


def min_sum_path(grid):
    memo = [len(grid) * [-1] for i in range(len(grid[0]))]
    i, j = 0, 0
    return min_path_sum(grid, memo, i, j)


test_case = [ [1,3,1],
  [1,5,1],
  [4,2,1]
]

print(min_sum_path(test_case))
