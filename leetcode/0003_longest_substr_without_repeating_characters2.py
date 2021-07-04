from functools import partial
from copy import deepcopy
import random
'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr_set = set()
        longest_size = 0
        temp_size = 0
        left = 0
        for right, letter in enumerate(s):
            if letter in substr_set:
                longest_size = max(temp_size, longest_size)
                while letter in substr_set:
                    substr_set.remove(s[left])
                    left += 1
                    temp_size -= 1
            substr_set.add(letter)
            temp_size += 1
        return max(longest_size, temp_size)

s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))


matrix = []
for i in range(3):
    matrix.append([1,2,3,4,5])

[print(row) for row in matrix]


copy = deepcopy(matrix)

print()
[print(element) for element in [row for row in matrix]]

test = [[0 for j in range(3)] for i in range(5)]
[print(row) for row in test]


