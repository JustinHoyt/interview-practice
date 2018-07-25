'''
https://www.hackerrank.com/contests/cs1300-odd-2014/challenges/array-rotation
'''
def rotate_90_in_place(nums):
    size = len(nums[0])
    for i in range(0, size-1):
        for j in range(i, size-1-i):
            p1 = nums[i][j]
            p2 = nums[j][size-1-i]
            p3 = nums[size-1-i][size-1-j]
            p4 = nums[size-1-j][i]
            nums[j][size-1-i] = p1
            nums[size-1-i][size-1-j] = p2
            nums[size-1-j][i] = p3
            nums[i][j] = p4


matrix = [
    [1, 6, 7, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

rotate_90_in_place(matrix)
for i in range(len(matrix[0])):
    print(matrix[i])
