'''
https://www.hackerrank.com/challenges/2d-array/problem
'''


def calc_hourglass(arr, row, col):
    return (arr[row - 1][col - 1] +
            arr[row - 1][col] +
            arr[row - 1][col + 1] +
            arr[row][col] +
            arr[row + 1][col - 1] +
            arr[row + 1][col] +
            arr[row + 1][col + 1])


def hourglass_sum(arr):
    best_sum = float("-inf")
    for row in range(1, len(arr) - 1):
        for col in range(1, len(arr[row]) - 1):
            best_sum = max(best_sum, calc_hourglass(arr, row, col))
    return best_sum


input = [
    [-9, -9, -9, 1, 1, 1],
    [0, -9, 0, 4, 3, 2],
    [-9, -9, -9, 1, 2, 3],
    [0, 0, 8, 6, 6, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]

print(hourglass_sum(input))
