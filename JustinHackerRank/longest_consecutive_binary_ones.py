def long_consecutive_binary_ones(num):
    bin_num = bin(num)[2:]
    best = 0
    sofar = 0
    for digit in bin_num:
        if digit == '1':
            sofar += 1
        else:
            best = max(best, sofar)
            sofar = 0
    return max(best, sofar)


num = 13
print(long_consecutive_binary_ones(num))
