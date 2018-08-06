def find_max_sum(arr):
    incl = 0
    excl = 0
    best = 0

    for next_number in arr:
        best = max(excl, incl)
        incl = excl + next_number
        excl = best

    return max(excl, incl)


# Driver program to test above function
arr = [5, 5, 10, 100, 10, 5]
print(find_max_sum(arr))
