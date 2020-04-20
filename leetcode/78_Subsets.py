from typing import List
import sys
# sys.setrecursionlimit(1500)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        def generate_subsets(subset, i):
            if i == len(nums):
                result.append(subset)
                return

            generate_subsets(subset, i + 1)
            new_subset = subset[:]
            new_subset.append(nums[i])
            generate_subsets(new_subset, i + 1)

        for i, num in enumerate(nums):
            generate_subsets(nums[i:i+1], i+1)

        return result

print(Solution().subsets([1,2,3]))
