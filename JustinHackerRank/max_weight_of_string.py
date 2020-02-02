'''
Given a binary string, you can transform it by toggling 1s to 0s and vice versa. You can make as many transformations as you want. Find out the maximum string weight you can get with given string as explained below:
Given 3 numbers:

Weight of a single pair = p
Weight of a single character = s
Weight of a single transformation = t
Note:

Weight of the transformed string = p + s - t.
A character in a string can be counted only once - either for a pair or a single character.
2 adjacent characters are a pair only if they are different, i.e. 00 and 11 don't form a pair but 01 and 10 do.
Test cases:

Input: p, s, t, string = 4, 2, 1, "110"
Output: 6

Input: p, s, t, string = 4, 1, 1, "00"
Output: 3

Input: p, s, t, string = 4, 1, 1, "011"
Output: 5

Input: p, s, t, string = 4, 1, 1, "0000011"
Input: p, s, t, string = 4, 1, 1, "0101011"
Output: 11
'''

def max_string(string, pair_weight, char_weight, transform_weight):
    memo={}

    def max_string_rec(string, idx=0, is_transformed=False):
        #base case
        if idx >= len(string):
            return 0
        key = (idx, is_transformed)
        if key in memo:
            return memo[key]

        # transform the index at a cost and don't move place. only do this once per index
        if not is_transformed:
            new_string = string
            new_string[idx] = 1 if new_string[idx] == 0 else 0
            transform_val = max_string_rec(new_string, idx, True) - transform_weight

        # evaluate a single number
        single_val = max_string_rec(string, idx+1) + char_weight

        # evaluate a pair if it is indeed a pair
        if string[idx] != string[idx+1]:
            pair_val = max_string_rec(string, idx+2) + pair_weight

        memo[key] = max(transform_val, single_val, pair_val)
        return memo[key]

    return max_string_rec(string)

print(max_string("0000011",4, 1, 1))
