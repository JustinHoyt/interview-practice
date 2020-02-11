def binary_search(nums, target, midpoint, left_bound, right_bound):
    if target == nums[midpoint]:
        return midpoint
    if right_bound == left_bound:
        return -1
    elif target < nums[midpoint]:
        if (target < nums[left_bound] and
                nums[left_bound] < nums[midpoint]): # go right
            left_bound = midpoint + 1
            midpoint = ((right_bound - left_bound) // 2) + left_bound
            return binary_search(nums, target, midpoint, left_bound, right_bound)
        else: # go left
            right_bound = midpoint - 1
            midpoint = ((right_bound - left_bound) // 2) + left_bound
            return binary_search(nums, target, midpoint, left_bound, right_bound)
    else:
        if (target > nums[right_bound] and
                nums[midpoint] < nums[right_bound]): # go left
            right_bound = midpoint - 1
            midpoint = ((right_bound - left_bound) // 2) + left_bound
            return binary_search(nums, target, midpoint, left_bound, right_bound)
        else: # go right
            left_bound = midpoint + 1
            midpoint = ((right_bound - left_bound) // 2) + left_bound
            return binary_search(nums, target, midpoint, left_bound, right_bound)


def find(nums, target):
    if len(nums) == 0:
        return -1
    left_bound = 0
    right_bound = len(nums) - 1
    midpoint = (len(nums) - 1) // 2
    return binary_search(nums, target, midpoint, left_bound, right_bound)


nums1 = [47, 48, 52, 98, 7, 8, 9, 12, 15, 20, 25, 30]
print(find(nums1, 98))
nums2 = [3, 4, 5, 6, 7, 8, 9, 12, 15, 20, 1, 2]
print(find(nums2, 4))
print(find(nums2, 1))
print(find(nums2, 89))
nums3 = [1]
print(find(nums3, 1))
nums4 = []
print(find(nums4, 1))
