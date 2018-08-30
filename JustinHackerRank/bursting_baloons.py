'''
https://leetcode.com/problems/burst-balloons/description/
'''
def print_memo(memo):
    for item in memo:
        print(str(item) + ": " + str(memo[item]))
        input()
    for i in range(5):
        print()


def product_of(nums, left, own, right):
    size = len(nums)
    result = nums[own]
    if left >= 0:
        result *= nums[left]
    if right < size:
        result *= nums[right]
    return result


def max_coins(nums, start, end, memo):
    key = (start, end)
    result = 0

    # print_memo(memo)

    if key in memo:
        return memo[key]
    if end - start == 0:
        result = product_of(nums, start-1, start, start+1)
    else:
        opt1 = max_coins(nums, start, end-1, memo) + \
            product_of(nums, start-1, end, end+1)
        opt2 = max_coins(nums, start+1, end, memo) + \
            product_of(nums, start-1, start, end+1)
        result = max(opt1, opt2)

    memo[key] = result
    return result


def pop_balloons(balloons):
    memo = {}
    start = 0
    end = len(balloons) - 1
    return max_coins(balloons, start, end, memo)


balloons = [3, 1, 5, 8]
print(pop_balloons(balloons))
