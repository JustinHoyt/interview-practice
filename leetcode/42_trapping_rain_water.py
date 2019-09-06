from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        left_best = height[0]
        right_best = height[-1]
        left_idx = 0
        right_idx = len(height) - 1
        count = 0

        while left_idx < right_idx:
            lowest_bound = min(left_best, right_best)
            if height[left_idx] < height[right_idx]:
                if height[left_idx] < lowest_bound:
                    count += lowest_bound - height[left_idx]
                left_idx += 1
                left_best = max(height[left_idx], left_best)
            else:
                if height[right_idx] < lowest_bound:
                    count += lowest_bound - height[right_idx]
                right_idx -= 1
                right_best = max(height[right_idx], right_best)

        return count

sol = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trap(height))
