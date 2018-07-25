'''
https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/
'''


def min_difference(nums):
    nums.sort()
    lowest = float('INF')
    for i in range(len(nums) - 1):
        lowest = min(lowest, abs(nums[i] - nums[i+1]))
    return lowest


print(min_difference([-20,-2,-4,5]))
