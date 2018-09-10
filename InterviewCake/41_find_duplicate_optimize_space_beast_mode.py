def find_duplicates(nums):
    duplicate = 0
    for i in range(len(nums)):
        if nums[nums[i]-1] < 0:
            duplicate = abs(nums[nums[i]-1])
            break
        else:
            nums[nums[i]-1] = - nums[nums[i]-1]
    for i in range(len(nums)):
        nums[i] = abs(nums[i])
    return duplicate


nums = [3, 4, 2, 3, 1, 5]
print(find_duplicates(nums))
print(nums)
