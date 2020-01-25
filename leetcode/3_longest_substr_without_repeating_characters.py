'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

class Solution:
    def length_of_longest_substring_set(self, s: str) -> int:
        letter_set = set()
        longest_length = 0
        curr_length = 0
        left = 0
        for right, letter in enumerate(s):
            if letter in letter_set:
                longest_length = max(longest_length, curr_length)
                while letter in letter_set:
                    letter_set.remove(s[left])
                    left += 1
                    curr_length -= 1
            curr_length += 1
            letter_set.add(letter)
            print(letter_set)

        return max(longest_length, curr_length)

    def length_of_longest_substring_map(self, s: str) -> int:
        most_recent_letter_idx_map = {}
        longest_length = 0
        curr_length = 0
        left = 0
        for right, letter in enumerate(s):
            if letter in most_recent_letter_idx_map:
                longest_length = max(longest_length, curr_length)
                if most_recent_letter_idx_map[letter] >= left:
                    left = most_recent_letter_idx_map[letter] + 1
                most_recent_letter_idx_map[letter] = right
                curr_length = right - left + 1
            else:
                curr_length += 1
                most_recent_letter_idx_map[letter] = right
        longest_length = max(curr_length, longest_length)
        return longest_length

sol = Solution()
problem = "QRACAR"
print(sol.length_of_longest_substring_map(problem))
# problem = "pwwkew"
# print(sol.length_of_longest_substring_map(problem))
# problem = "abba"
# print(sol.length_of_longest_substring_map(problem))
# problem = "a"
# print(sol.length_of_longest_substring_map(problem))
# problem = "bbbbb"
# print(sol.length_of_longest_substring_map(problem))
