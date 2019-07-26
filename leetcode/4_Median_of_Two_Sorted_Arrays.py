class Solution:
    '''
    size = 5
    i = 2
    j = 1
         v
    [1,2,5]
       v
    [3,4]

    size = 6
    i = 2
    j = 1
       v
    [1,2,5]
     v
    [3,4,6]
    '''
    def findMedianSortedArrays(self, nums1, nums2):
        i = 0
        j = 0
        last_val = 0
        second_last_val = 0
        size = len(nums1) + len(nums2)
        while (i + j <= size // 2 and
               i < len(nums1) and
               j < len(nums2)):
            if nums1[i] <= nums2[j]:
                second_last_val = last_val
                last_val = nums1[i]
                i += 1
            else:
                second_last_val = last_val
                last_val = nums2[j]
                j += 1

        while (i + j <= size // 2 and
               i < len(nums1)):
            second_last_val = last_val
            last_val = nums1[i]
            i += 1

        while (i + j <= size // 2 and
               j < len(nums2)):
            second_last_val = last_val
            last_val = nums2[j]
            j += 1

        if size % 2 == 0:
            return (last_val + second_last_val) / 2
        else:
            return last_val

sol = Solution()
print(sol.findMedianSortedArrays([1,2], [4,5,6,7]))
print(sol.findMedianSortedArrays([1], [4,5,6,7]))
print(sol.findMedianSortedArrays([], [4,5,6,7]))
print(sol.findMedianSortedArrays([7], []))
