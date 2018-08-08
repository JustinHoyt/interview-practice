def high_substr_rec(str1, str2, start1, start2, end1, end2, memo, found):

    key = str(start1) + "-" + str(end1) + " " + str(start1) + "-" + str(end2)
    if key in memo:
        return memo[key]
    high = 0
    if start1 == end1 or start2 == end2:
        return 0

    if found:
        return 0
    opt1 = high_substr_rec(str1, str2, start1+1, start2, end1, end2, memo, found)
    if str1[start1] == str2[start2]:
        opt1 += 1
        found = True
    opt2 = high_substr_rec(str1, str2, start1, start2+1, end1, end2, memo, found)
    if str1[start1] == str2[start2]:
        opt2 += 1
        found = True
    opt3 = high_substr_rec(str1, str2, start1, start2, end1-1, end2, memo, found)
    if str1[end1] == str2[end2]:
        opt3 += 1
        found = True
    opt4 = high_substr_rec(str1, str2, start1, start2, end1, end2-1, memo, found)
    if str1[end1] == str2[end2]:
        opt4 += 1
        found = True

    high = max(opt1, opt2, opt3, opt4)
    memo[key] = high
    return high


def high_substr(str1, str2):
    found = False
    return high_substr_rec(str1, str2, 0, 0, len(str1)-1, len(str2)-1, {}, found)


# print(high_substr("shinchan", "noharaaa"))
print(high_substr("abdcc", "abcde"))

