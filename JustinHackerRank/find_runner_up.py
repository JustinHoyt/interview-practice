n = input()
nums = [int(x) for x in input().split(" ")]

best = nums[0]
second_best = nums[0]
for num in nums:
    if num > best:
        second_best = best
        best = num
    elif num > second_best and num != best:
        second_best = num

print(second_best)
