def high_substr_rec(str1, str2, i, j, memo):
    size = len(str1)
    if i >= size or j >= size:
        return 0

    if memo[i][j] != -1:
        return memo[i][j]

    if i == size-1 and j == size-1:
        if str1[i] == str2[j]:
            return 1
        else:
            return 0

    below = high_substr_rec(str1, str2, i+1, j, memo)
    right = high_substr_rec(str1, str2, i, j+1, memo)
    below_right = high_substr_rec(str1, str2, i+1, j+1, memo)
    memo[i][j] = max(right, below)
    if below_right == memo[i][j] and str1[i] == str2[j]:
        memo[i][j] += 1

    return memo[i][j]


def high_substr(str1, str2):
    memo = [[-1] * len(str1) for x in range(len(str1))]
    return high_substr_rec(str1, str2, 0, 0, memo)


print(high_substr("a", "a"))
print(high_substr("hna", "hna"))
print(high_substr("abdcc", "abcde"))
print(high_substr("shinchan", "noharaaa"))
print(high_substr("abcdef", "fbdamn"))
print(high_substr("harry", "sally"))
print(high_substr("aa", "bb"))
