from timeit import default_timer as timer

# optimal generative approach
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

# Dynamic programming approach for checking every number up to the n'th ugly number.
# Despite using DP, this solution is still too slow because of the exponential growth of 
# the distance between ugly numbers.
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

start = timer()
print("generative for n=1690 -", nth_ugly_num(1690))
end = timer()
print(end - start)

start = timer()
print("DP checking all nums for n=1000 -", nth_ugly_num_DP(1000))
end = timer()
print(end - start)
