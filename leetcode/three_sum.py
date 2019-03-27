'''
Given an array of distinct elements. The task is to find triplets in array whose sum is zero
'''
def sum_to_zero(nums):
    num_set = set()
    for num in nums:
        num_set.add(num)
    for i in range(len(nums)):
        for j in range(len(nums)):
            sum = nums[i] + nums[j]
            if -sum in num_set:
                print(-sum, nums[i], nums[j])


nums = [1,-2,1,3,3,1,2,-9, 0]
print(sum_to_zero(nums))
