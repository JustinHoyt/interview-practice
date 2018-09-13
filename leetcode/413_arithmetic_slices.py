'''
https://leetcode.com/problems/arithmetic-slices/description/

A sequence of number is called arithmetic if it consists of at least
three elements and if the difference between any two consecutive
elements is the same. Return the number of arithmetic slices
'''
def num_arithmetic_slices(nums):
    count = 0
    offset = nums[1] - nums[0]
    seq_len = 1

    for i in range(1, len(nums)-1):
        if nums[i+1] - nums[i] == offset:
            seq_len += 1
        else:
            count += (seq_len) * (seq_len-1) // 2
            seq_len = 1
            offset = nums[i+1] - nums[i]
    count += (seq_len) * (seq_len-1) // 2
    return count


nums = [1, 2, 3, 4, 5, 6, 8, 10, 12]
# nums = [1, 1, 1, 1, 1]
print(num_arithmetic_slices(nums))
