def give_candies(students, memo, current, prev):
    key = str(current)
    if key in memo:
        return memo[key]

    if len(students) <= current or current < 0:
        return 0

    left = 0
    right = 0
    if current - 1 != prev and current-1 >= 0:
        left = give_candies(students, memo, current-1, current)
        if students[current] > students[current-1]:
            left += 1

    if current + 1 != prev and current+1 < len(students):
        right = give_candies(students, memo, current+1, current)
        if students[current] > students[current+1]:
            right += 1

    result = left + right
    # result = max(left, right)
    memo[key] = result
    return result


def candies(students):
    memo = {}
    current = 0
    prev = -1
    return give_candies(students, memo, current, prev)


testcase1 = [4, 6, 4, 5, 6, 2]
print(candies(testcase1))
