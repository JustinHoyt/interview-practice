class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i, num in enumerate(nums):
            pass

print(Solution().subsets([1,2,3]))

'''
   R
 L
[1,2,3]

[
  []
  [1]
  [1,2]
  [1,2,3]
  [1,3]
  [2]
  [2,3]
  [3]
]

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''