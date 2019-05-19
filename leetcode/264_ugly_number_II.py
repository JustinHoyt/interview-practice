from timeit import default_timer as timer

def nth_ugly_num(n):
    ugly = [1]
    idx_2 = 0
    idx_3 = 0
    idx_5 = 0
    while n > 1:
        ugly_2 = 2 * ugly[idx_2]
        ugly_3 = 3 * ugly[idx_3]
        ugly_5 = 5 * ugly[idx_5]
        next_ugly = min(ugly_2, ugly_3, ugly_5)
        if next_ugly == ugly_2:
            idx_2 += 1
        if next_ugly == ugly_3:
            idx_3 += 1
        if next_ugly == ugly_5:
            idx_5 += 1
        ugly.append(next_ugly)
        n -= 1
    return ugly[-1]


def nth_ugly_num_DP(n):
    calculations = 0
    ugly_memo = {1, 2, 3, 4, 5}
    num = 5
    num_ugly = 5
    if n <= 5:
        return n
    while num_ugly <= n:
        if num % 2 == 0 and num // 2 in ugly_memo:
            calculations += 1
            ugly_memo.add(num)
            num_ugly += 1
        elif num % 3 == 0 and num // 3 in ugly_memo:
            calculations += 1
            ugly_memo.add(num)
            num_ugly += 1
        elif num % 5 == 0 and num // 5 in ugly_memo:
            calculations += 1
            ugly_memo.add(num)
            num_ugly += 1
        else:
            calculations += 1
        num += 1
    print("calculations:", calculations)
    return num - 1


# print("1th number is:", nth_ugly_num(1))
# print("2th number is:", nth_ugly_num(2))
# print("3th number is:", nth_ugly_num(3))
# print("4th number is:", nth_ugly_num(4))
# print("5th number is:", nth_ugly_num(5))
# print("6th number is:", nth_ugly_num(6))
# print("7th number is:", nth_ugly_num(7))
# print("8th number is:", nth_ugly_num(8))
# print("9th number is:", nth_ugly_num(9))
# print("10th number is:", nth_ugly_num(10))
# print("11th number is:", nth_ugly_num(11))
# print("12th number is:", nth_ugly_num(12))
# print("13th number is:", nth_ugly_num(13))
# print("14th number is:", nth_ugly_num(14))
# print("15th number is:", nth_ugly_num(15))
# print("16th number is:", nth_ugly_num(16))
# print("17th number is:", nth_ugly_num(17))
# print("100th number is:", nth_ugly_num(100))
# print("200th number is:", nth_ugly_num(200))
# print("400th number is:", nth_ugly_num(400))
# print("800th number is:", nth_ugly_num(800))

start = timer()
print("mine 1690 -", nth_ugly_num(1690))
end = timer()
print(end - start)

sample = 1000
start = timer()
print(sample, "-", nth_ugly_num_DP(sample))
end = timer()
print(end - start)
