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


nums1 = [1,-2,1,3,3,1,2,-9, 0]
nums2 = [1,-1,3,9]
print(sum_to_zero(nums1))
print(sum_to_zero(nums2))
