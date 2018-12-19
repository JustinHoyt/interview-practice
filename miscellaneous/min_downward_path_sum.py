'''
Given a 2D matrix of integers A. We want the minimum sum of a downward path through A.

Note: A downward path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.

'''
def min_downward_path_sum_rec(grid, i, j):
    if i == len(grid) or j == len(grid[0]):
        return float('inf')
    if i == len(grid) - 1:
        return grid[-1][j]
    lowest_path = min(min_downward_path_sum_rec(grid, i+1, j),
                      min_downward_path_sum_rec(grid, i+1, j+1),
                      min_downward_path_sum_rec(grid, i+1, j-1))
    return lowest_path + grid[i][j]


def min_downward_path_sum(grid):
    i = 0
    j = 0
    return min_downward_path_sum_rec(grid, i, j)


grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

print(min_downward_path_sum(grid), 12)

grid2 = [
    [-10,5,2],
    [-1,-2,3],
]

print(min_downward_path_sum(grid2), -12)
