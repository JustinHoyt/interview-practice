def binary_search_rec(nums, target, low, high):
    midpoint = low + (high - low) // 2
    if target == nums[midpoint]:
        return midpoint
    if target == nums[high]:
        return high
    if target > high or target < low:
        return -1
    elif target < nums[midpoint]:
        return binary_search_rec(nums, target, low, midpoint)
    elif target > nums[midpoint]:
        return binary_search_rec(nums, target, midpoint, high)

def binary_search(nums, target):
    return binary_search_rec(nums, target, 0, len(nums)-1)

nums = [1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 45]
target = 45
print(binary_search(nums, target))
