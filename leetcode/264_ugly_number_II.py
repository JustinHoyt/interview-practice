def nth_ugly_num_DP(n):
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


print("3:", nth_ugly_num_DP(3))
print("5:", nth_ugly_num_DP(5))
print("7:", nth_ugly_num_DP(7))
print("11:", nth_ugly_num_DP(11))
print("12:", nth_ugly_num_DP(12))
print("13:", nth_ugly_num_DP(13))
print("14:", nth_ugly_num_DP(14))
print("15:", nth_ugly_num_DP(15))
print("16:", nth_ugly_num_DP(16))
print("17:", nth_ugly_num_DP(17))
print("100:", nth_ugly_num_DP(100))
print("200:", nth_ugly_num_DP(200))
print("400:", nth_ugly_num_DP(400))
print("800:", nth_ugly_num_DP(800))


def nth_ugly_num(n):
    memo = [1, 2, 3, 4, 5]
    if n < len(memo):
        return n
    for _ in range(n-5):
        next_ugly = float('inf')
        for memo_idx in range(len(memo)):
            ugly_primes = [2, 3, 5]
            for ugly_prime in ugly_primes:
                possible_ugly = memo[memo_idx] * ugly_prime
                if(possible_ugly > memo[-1] and
                   possible_ugly < next_ugly):
                    next_ugly = possible_ugly
        memo.append(next_ugly)
    return memo[-1]


print("1:", nth_ugly_num(1))
print("2:", nth_ugly_num(2))
print("3:", nth_ugly_num(3))
print("4:", nth_ugly_num(4))
print("5:", nth_ugly_num(5))
print("6:", nth_ugly_num(6))
print("7:", nth_ugly_num(7))
print("8:", nth_ugly_num(8))
print("9:", nth_ugly_num(9))
print("10:", nth_ugly_num(10))
print("11:", nth_ugly_num(11))
print("12:", nth_ugly_num(12))
print("13:", nth_ugly_num(13))
print("14:", nth_ugly_num(14))
print("15:", nth_ugly_num(15))
print("16:", nth_ugly_num(16))
print("17:", nth_ugly_num(17))
print("100:", nth_ugly_num(100))
print("200:", nth_ugly_num(200))
print("400:", nth_ugly_num(400))
print("800:", nth_ugly_num(800))
print("1690:", nth_ugly_num(1690))
