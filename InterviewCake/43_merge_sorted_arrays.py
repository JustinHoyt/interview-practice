def merge(nums1, nums2):
    front1 = 0
    front2 = 0
    merge_list = []

    while front1 < len(nums1) and front2 < len(nums2):
        if nums1[front1] < nums2[front2]:
            merge_list.append(nums1[front1])
            front1 += 1
        else:
            merge_list.append(nums2[front2])
            front2 += 1
    for i in range(front1, len(nums1)):
        merge_list.append(nums1[front1])
        front1 += 1
    for i in range(front2, len(nums2)):
        merge_list.append(nums2[front2])
        front2 += 1
    return merge_list


nums1 = [1,2,5,7,9,10]
nums2 = [3,4,6,12,15]
print(merge(nums1, nums2))
