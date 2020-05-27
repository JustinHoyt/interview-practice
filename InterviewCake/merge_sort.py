'''
Created on Nov 4, 2016

@author: justinhoyt
'''
from random import shuffle

def merge(left, right):
    result = []
    front = 0
    while front < len(left) and front < len(right):
        if left[front] < right[front]:
            result.append(left[front])
            del left[front]
        else:
            result.append(right[front])
            del right[front]
    if front < len(left):
        result.extend(left[front:])
    if front < len(right):
        result.extend(right[front:])
    return result


def merge_sort(array):
    if len(array) < 2:
        return array

    middle = len(array) // 2
    left = merge_sort(array[middle:])
    right = merge_sort(array[:middle])
    return merge(left, right)


big_list = list(range(10000))
shuffle(big_list)
# print(big_list)
print(merge_sort(big_list)[1])