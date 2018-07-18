def prod_array(nums):
    totals = [1] * len(nums)
    left = [1] * len(nums)
    right = [1] * len(nums)

    for i in range(1, len(nums)):
        left[i] = (left[i-1] * nums[i-1])
        print(left)
    for i in range(len(nums) - 2, -1, -1):
        right[i] = (right[i+1] * nums[i+1])
        print(right)
    for i in range(len(nums)):
        totals[i] = right[i] * left[i]
    return totals


print(prod_array([10, 3, 5, 6, 2]))
