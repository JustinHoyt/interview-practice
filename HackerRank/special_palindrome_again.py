def num_special_palindromes(word):
    count = len(word)

    for i in range(1, len(word)-1):
        offset = 2
        if word[i-1] == word[i+1] and word[i] != word[i+1]:
            count += special_palindrome(word, i, offset) + 1

    i = 0
    while i < len(word)-1:
        j = i + 1
        occurances = 1
        while(j < len(word) and word[i] == word[j]):
            occurances += 1
            j += 1
        count += occurances * (occurances-1) / 2
        i = j
    return count


def special_palindrome(word, i, offset):
    if i - offset >= 0 and i + offset < len(word):
        if (word[i-offset] == word[i+offset] and
                word[i + offset - 1] == word[i+offset]):
            return special_palindrome(word, i, offset+1) + 1
    return 0


word1 = "mnonoopooo"
print(num_special_palindromes(word1))
word2 = "aaaa"
print(num_special_palindromes(word2))
