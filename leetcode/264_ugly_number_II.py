def nth_ugly_num(n):
    ugly_memo = {1, 2, 3, 4, 5}

    num = 5
    num_ugly = 5
    if n <= 5:
        return n
    while num_ugly <= n:
        if num % 2 == 0 and num // 2 in ugly_memo:
            ugly_memo.add(num)
            num_ugly += 1
        elif num % 3 == 0 and num // 3 in ugly_memo:
            ugly_memo.add(num)
            num_ugly += 1
        elif num % 5 == 0 and num // 5 in ugly_memo:
            ugly_memo.add(num)
            num_ugly += 1
        num += 1
    return num - 1


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
print(nth_ugly_num(100))
print(nth_ugly_num(200))
print(nth_ugly_num(400))
print(nth_ugly_num(800))
