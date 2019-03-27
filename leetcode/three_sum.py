'''
Determine if any 3 integers in an array sum to 0.
'''

def brute_force_sum_to_zero(nums):
    for i in range(0, len(nums)):
        for j in range (i, len(nums)):
            for k in range(j, len(nums)):
                if ((nums[i] + nums[j] + nums[k]) == 0):
                    return True
    return False


def sum_to_zero(nums):
    num_set = set()
    for num in nums:
        num_set.add(num)
    for i in range(len(nums)):
        for j in range(len(nums)):
            sum = nums[i] + nums[j]
            if -sum in num_set:
                return True
    return False


def walking_solution(nums):
    nums = sorted(nums)
    # enumerate fetches both index and value
    for i, num in enumerate(nums):
        min_index = i
        max_index = len(nums) - 1
        while (min_index <= max_index):
            # if min + max > target then max can't be part of solution
            if ((nums[min_index] + nums[max_index]) > -num):
                max_index -= 1
            # if min + max < target then min can't be part of solution
            elif ((nums[min_index] + nums[max_index]) < -num):
                min_index += 1
            else:
                # valid solution
                print(num, nums[min_index],nums[max_index])
                break


nums1 = [1,-2,3,2,-9,-3,0]
nums2 = [1,-1,3,9]
print(sum_to_zero(nums1))
print(sum_to_zero(nums2))
print(walking_solution(nums1))
