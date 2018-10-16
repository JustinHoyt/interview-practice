def nth_ugly_num(n):
    memo = [True, True, True, True, True]

    num = 5
    count = 5
    if n <= 5:
        return n
    while count != n+1:
        if num % 2 == 0:
            memo.append(memo[num//2])
            if memo[-1] is True:
                count += 1
        elif num % 3 == 0:
            memo.append(memo[num//3])
            if memo[-1] is True:
                count += 1
        elif num % 5 == 0:
            memo.append(memo[num//5])
            if memo[-1] is True:
                count += 1
        else:
            memo.append(False)
        num += 1
    return len(memo) - 1


print(nth_ugly_num(3))
print(nth_ugly_num(5))
print(nth_ugly_num(7))
print(nth_ugly_num(11))
print(nth_ugly_num(12))
print(nth_ugly_num(13))
print(nth_ugly_num(14))
print(nth_ugly_num(15))
print(nth_ugly_num(16))
print(nth_ugly_num(17))
print(nth_ugly_num(800))
