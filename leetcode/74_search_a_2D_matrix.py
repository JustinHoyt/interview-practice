def find(nums, target):
    row_idx = find_row(nums, target, 0, len(nums)-1)
    print(row_idx)
    return find_in_row(nums, target, row_idx, 0, len(nums)-1)


def find_row(nums, target, row_start, row_end):
    if row_start > row_end:
        return -1
    midpoint = row_start + (row_end - row_start) // 2
    if target <= nums[midpoint][len(nums[0])-1]:
        if target >= nums[midpoint][0]:
            return midpoint
        else:
            return find_row(nums, target, row_start, midpoint-1)
    else:
        return find_row(nums, target, midpoint+1, row_end)


def find_in_row(nums, target, row, col_start, col_end):
    if row == -1 or col_start > col_end:
        return False
    midpoint = col_start + (col_end - col_start) // 2
    if target == nums[row][midpoint]:
        print(midpoint)
        return True
    elif target < nums[row][midpoint]:
        return find_in_row(nums, target, row, col_start, midpoint-1)
    else:
        return find_in_row(nums, target, row, midpoint+1, col_end)


nums = [
    [1, 3, 5, 7, 12],
    [10, 11, 16, 20, 25],
    [27, 28, 34, 50, 60],
    [63, 70, 74, 78, 80],
    [82, 93, 95, 97, 100],
]

print(find(nums, 1))
