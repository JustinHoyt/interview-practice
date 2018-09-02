def explore_land(grid, row, col):
    if row < len(grid) and \
            row >= 0 and \
            col < len(grid[0]) and \
            col >= 0 and \
            grid[row][col] == 1:
        grid[row][col] = 0
        explore_land(grid, row+1, col)
        explore_land(grid, row-1, col)
        explore_land(grid, row, col+1)
        explore_land(grid, row, col-1)


def count_islands(grid):
    islands_count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                explore_land(grid, row, col)
                islands_count += 1
    return islands_count


grid = [[1, 1, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [1, 1, 1, 1],
]

print(count_islands(grid))
