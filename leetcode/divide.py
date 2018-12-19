'''
Divide without division or modulo
'''
# Linear solution
def divide_linear(num, den):
    remaining = num
    quotient = 0
    while remaining >= den:
        remaining -= den
        quotient += 1
    return (quotient, remaining)


# Times two solution
def find_quotient_climb(remaining, den):
    quotient = 0
    if remaining < den:
        return 0
    i = 0
    while remaining - den * 2**i >= 0:
        remaining -= den * 2**i
        quotient += 2**i
        i += 1
    return quotient + find_quotient_climb(remaining, den)

def divide_climb(num, den):
    quotient = find_quotient_climb(num, den)
    remaining = num - quotient * den
    return (quotient, remaining)


# Binary search divide
def find_quotient_binary_search(num, den, high, low):
    midpoint = low + ((high - low) >> 1)
    remaining = num - midpoint * den
    if remaining < den and remaining >= 0:
        return midpoint
    if remaining < 0:
        high = midpoint
    else:
        low = midpoint
    return find_quotient_binary_search(num, den, high, low)

def divide_binary_search(num, den):
    quotient = find_quotient_binary_search(num, den, num, 0)
    remainder = num - quotient * den
    return quotient, remainder


print(divide_linear(931, 3))
print(divide_climb(931, 3))
print(divide_binary_search(931, 3))
