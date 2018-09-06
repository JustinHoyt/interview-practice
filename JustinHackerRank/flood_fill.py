def flood_fill_rec(grid, row, col, color_to_paint):
    if (row < len(grid) and row >= 0 and
            col < len(grid[0]) and col >= 0 and
            grid[row][col] != color_to_paint):
        grid[row][col] = color_to_paint
        flood_fill_rec(grid, row+1, col, color_to_paint)
        flood_fill_rec(grid, row-1, col, color_to_paint)
        flood_fill_rec(grid, row, col+1, color_to_paint)
        flood_fill_rec(grid, row, col-1, color_to_paint)

def flood_fill(grid, row, col):
    if row >= len(grid) or col >= len(grid[0]):
        return "Coordinate not in grid"
    color_to_paint = 0
    if grid[row][col] == 0:
        color_to_paint = 1
    flood_fill_rec(grid, row, col, color_to_paint)
    return "Success"


grid1 = [[0, 1, 0, 1],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0]]

print(flood_fill(grid1, 2, 2))
grid2 = []
print(flood_fill(grid2, 0, 0))
for row in grid1:
    print(row)
