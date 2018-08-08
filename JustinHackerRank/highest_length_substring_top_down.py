def high_substr_rec(str1, str2, memo):

    key = str1 + "-" + str2
    if key in memo:
        return memo[key]
    high = 0
    if len(str1) == 0 or len(str2) == 0:
        return 0

    if str1 == str2:
        return len(str1)

    for i in range(len(str1)):
        temp_str1 = str1[:i]
        if i+1 < len(str1):
            temp_str1 += str1[i+1:]
        high = max(high_substr_rec(temp_str1, str2, memo), high)

    for i in range(len(str2)):
        temp_str2 = str2[:i]
        if i+1 < len(str1):
            temp_str2 += str2[i+1:]
        high = max(high_substr_rec(str1, temp_str2, memo), high)

    memo[key] = high
    return high


def high_substr(str1, str2):
    return high_substr_rec(str1, str2, {})


print(high_substr("hna", "hna"))
print(high_substr("abdcc", "abcde"))
print(high_substr("shinchan", "noharaaa"))
print(high_substr("abcdef", "fbdamn"))
print(high_substr("harry", "sally"))
print(high_substr("aa", "bb"))
