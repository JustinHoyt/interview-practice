class Solution:
    def permuteUnique(self, nums):
        ans = [[]]
        for num in nums:
            new_ans = []
            for permutation in ans:
                for i in range(len(permutation) + 1):
                    new_ans.append(permutation[:i] + [num] + permutation[i:])

                    # if we have the same num for our i'th permutation we want to break out
                    # to avoid duplicate permutations
                    if i < len(permutation) and permutation[i] == num:
                        break
            ans = new_ans
        return ans

print(Solution().permuteUnique([1,1,2]))