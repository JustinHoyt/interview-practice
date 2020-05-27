def merge(nums, start, end):
    result = []
    while True:
        if nums1[0] < nums2[0]:
            result.append(nums1[0])
            del nums1[0]
        else:
            result.append(nums2[0])
            del nums2[0]
    while len(nums1) > 0:
        result.append(nums1[0])
        del nums1[0]
    while len(nums2) > 0:
        result.append(nums2[0])
        del nums2[0]

    print(result)
    return result

def merge_sort(nums):
    if len(nums) == 1:
        return nums
    midpoint = len(nums) // 2
    left = merge_sort(nums, start, midpoint)
    right = merge_sort(nums, midpoint, end)
    merge(left, right)
    return nums

nums = [10,5,9,100,23,532,1,23,90]
print(merge_sort(nums))
