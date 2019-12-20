def num_subarrays_with_odd_elements(nums, target_odd):
    i = 0
    j = 0
    num_odd = 0
    count = 0
    while j < len(nums):
        if num_odd == target_odd:
            count += 1

        if nums[j] % 2 == 1:
            num_odd += 1

        print(num_odd, target_odd)
        print(i, j)
        print()
        # input()
        if num_odd < target_odd:
            if nums[j] % 2 == 1:
                num_odd += 1
            j += 1
        else:
            if nums[i] % 2 == 1:
                num_odd -= 1
            i += 1

    return count

# num_odd = 2

# nums = [2, 5, |6, 9|]
nums = [2, 5, 6, 9]
m = 2
print(num_subarrays_with_odd_elements(nums, m))
