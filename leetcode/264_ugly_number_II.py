from timeit import default_timer as timer


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


def nth_ugly_num(n):
    calculation = 0
    memo = [1, 2, 3, 4, 5]
    start = 0
    if n < len(memo):
        return n
    for _ in range(n-5):
        next_ugly = float('inf')
        for memo_idx in range(start, len(memo)):
            ugly_primes = [2, 3, 5]
            for ugly_prime in ugly_primes:
                possible_ugly = memo[memo_idx] * ugly_prime
                calculation += 1
                if(possible_ugly > memo[-1] and
                   possible_ugly < next_ugly):
                    next_ugly = possible_ugly
        memo.append(next_ugly)
        if memo[start] * 5 <= next_ugly:
            start += 1
    print("calculations:", calculation)
    return memo[-1]


print("1th number is:", nth_ugly_num(1))
print("2th number is:", nth_ugly_num(2))
print("3th number is:", nth_ugly_num(3))
print("4th number is:", nth_ugly_num(4))
print("5th number is:", nth_ugly_num(5))
print("6th number is:", nth_ugly_num(6))
print("7th number is:", nth_ugly_num(7))
print("8th number is:", nth_ugly_num(8))
print("9th number is:", nth_ugly_num(9))
print("10th number is:", nth_ugly_num(10))
print("11th number is:", nth_ugly_num(11))
print("12th number is:", nth_ugly_num(12))
print("13th number is:", nth_ugly_num(13))
print("14th number is:", nth_ugly_num(14))
print("15th number is:", nth_ugly_num(15))
print("16th number is:", nth_ugly_num(16))
print("17th number is:", nth_ugly_num(17))
print("100th number is:", nth_ugly_num(100))
print("200th number is:", nth_ugly_num(200))
print("400th number is:", nth_ugly_num(400))
print("800th number is:", nth_ugly_num(800))

start = timer()
print("1690:", nth_ugly_num(1690))
end = timer()
print(end - start)
