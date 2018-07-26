from random import shuffle


def merge(left, right):
    print(left, end=' ')
    print(right)
    total = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            total.append(left[0])
            del left[0]
        else:
            total.append(right[0])
            del right[0]
    if len(left) > 0:
        total.extend(left[0:])
    if len(right) > 0:
        total.extend(right[0:])
    print(total)
    return total


def merge_sort(nums):
    if len(nums) < 2:
        return nums

    mid_point = len(nums)//2
    left = merge_sort(nums[:mid_point])
    right = merge_sort(nums[mid_point:])
    return merge(left, right)


# mylist = list(range(1000))
# shuffle(mylist)
mylist = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(merge_sort(mylist))
