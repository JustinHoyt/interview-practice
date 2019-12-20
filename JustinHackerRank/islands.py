def explore_land_with_is_visited_grid(grid, is_visited_grid, row, col):
    if row < len(grid) and \
            row >= 0 and \
            col < len(grid[0]) and \
            col >= 0 and \
            grid[row][col] == 1 and \
            is_visited_grid[row][col] == 0:
        is_visited_grid[row][col] = 1
        explore_land_with_is_visited_grid(grid, is_visited_grid, row+1, col)
        explore_land_with_is_visited_grid(grid, is_visited_grid, row-1, col)
        explore_land_with_is_visited_grid(grid, is_visited_grid, row, col+1)
        explore_land_with_is_visited_grid(grid, is_visited_grid, row, col-1)


def count_islands_with_is_visited_grid(grid):
    '''
    O(n*m) Time
    O(n*m) Space
    We use a data structure to keep track of visited
    pieces of land.
    '''
    is_visited_grid = [[0] * len(grid[0]) for x in range(len(grid))]
    islands_count = 0
    for row, _ in enumerate(grid):
        for col, _ in enumerate(grid[row]):
            if grid[row][col] == 1 and is_visited_grid[row][col] == 0:
                islands_count += 1
                explore_land_with_is_visited_grid(grid, is_visited_grid, row, col)
    return islands_count


def explore_land_mutate_input(grid, row, col):
    if (0 <= row < len(grid) and
            0 <= col < len(grid[0]) and
            grid[row][col] == 1):
        grid[row][col] = 0
        explore_land_mutate_input(grid, row+1, col)
        explore_land_mutate_input(grid, row-1, col)
        explore_land_mutate_input(grid, row, col+1)
        explore_land_mutate_input(grid, row, col-1)


def count_islands_mutate_input(grid):
    '''
    O(n*m) Time
    O(1) Space
    We are trading improved space in exchange for
    mutating the input, which is not a best practice
    '''
    islands_count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                explore_land_mutate_input(grid, row, col)
                islands_count += 1
    return islands_count


def explore_land_best(grid, row, col):
    if row < len(grid) and \
            row >= 0 and \
            col < len(grid[0]) and \
            col >= 0 and \
            grid[row][col] == 1:
        grid[row][col] = -1
        explore_land_best(grid, row+1, col)
        explore_land_best(grid, row-1, col)
        explore_land_best(grid, row, col+1)
        explore_land_best(grid, row, col-1)


def count_islands_best(grid):
    '''
    O(n*m) Time
    O(1) Space
    This is the best solution because it uses constant
    space and keeps the given grid in tact
    '''
    islands_count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                explore_land_best(grid, row, col)
                islands_count += 1
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == -1:
                grid[row][col] = 1
    return islands_count


grid = [[1, 1, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [1, 1, 1, 1],
]

print(count_islands_with_is_visited_grid(grid))
print(count_islands_best(grid))
print(count_islands_mutate_input(grid))
