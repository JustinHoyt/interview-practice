from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left_array, right_array):
            i = j = 0
            result = []

            while i < len(left_array) and j < len(right_array):
                if left_array[i] < right_array[j]:
                    result.append(left_array[i])
                    i += 1
                else:
                    result.append(right_array[j])
                    j += 1
            
            if i < len(left_array):
                result.extend(left_array[i:])
            elif j < len(right_array):
                result.extend(right_array[j:])
            
            return result
                
        def merge_sort(left=0, right=len(nums)-1) -> List[int]:
            if left == right:
                return [nums[left]]

            mid = (left + right) // 2

            left_array = merge_sort(left, mid)
            right_array = merge_sort(mid + 1, right)

            return merge(left_array, right_array)
            
        return merge_sort()

print(Solution().sortArray([5,2,3,1]))