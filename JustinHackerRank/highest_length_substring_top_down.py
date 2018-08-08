def high_substr_rec(str1, str2, str1_end, str2_end, memo):
    key = str(str1_end) + "-" + str(str2_end) + "-" + str()
    if key in memo:
        return memo[key]
    high = 0
    if str1_end == 0 or str2_end == 0:
        if str1[str1_end] == str2[str2_end]:
            return 1
        else:
            return 0

    opt1 = high_substr_rec(str1, str2, str1_end-1, str2_end, memo)
    opt2 = high_substr_rec(str1, str2, str1_end, str2_end-1, memo)
    if str1[str1_end] == str2[str2_end]:
        opt1 += 1
        opt2 += 1

    high = max(opt1, opt2)
    memo[key] = high
    return high


def high_substr(str1, str2):
    return high_substr_rec(str1, str2, len(str1)-1, len(str2)-1, {})


print(high_substr("shinchan", "noharaaa"))
