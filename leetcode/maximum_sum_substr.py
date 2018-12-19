def max_substr_sum_rec(nums, start, end, memo):
    key = (start, end)
    if memo[key]:
        return memo[key]
    if len(nums) == start:
        return 0

    result = max(max_substr_sum_rec(nums, start + 1) + nums[start],  nums[start])
    memo[key] = result
    return result


def max_substr_sum(nums):
    start = 0
    memo = {}
    for i in range(nums):
        for j in range(i, nums):
            if i == j:
                memo[(i,j)] = nums[i]
            memo[(i,j)] = memo[(i,j-1)] + nums[j]
    return max(memo)


nums = [3, 1, -2, 10, -1, -5]
print(max_substr_sum(nums))
