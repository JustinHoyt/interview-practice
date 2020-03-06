def next_char(word, idx):
    backspace_count = 0
    while idx >= 0 and (word[idx] == "<" or backspace_count > 0):
        if word[idx] == "<":
            backspace_count += 1
        else:
            backspace_count -= 1
        idx -= 1

    return idx

def is_same_output(str1, str2):
    i = len(str1) - 1
    j = len(str2) - 1

    while i >= 0 and j >= 0:
        i = next_char(str1, i)
        j = next_char(str2, j)

        if i < 0 or j < 0:
            break

        if str1[i] != str2[j]:
            return False

        i -= 1
        j -= 1

    if i >= 0:
        i = next_char(str1, i)
        return i == -1
    if j >= 0:
        j = next_char(str2, j)
        return j == -1
    return True



# True
print(is_same_output("world", "<<worrr<<ld"))
print(is_same_output("", "<<wr<<"))
print(is_same_output("w<<i", "c<<irrr<<ld<<<"))

# False
print(is_same_output("<<<", "<<worrr<<ld"))
print(is_same_output("w<<i", "c<<irrr<<ldd<<<"))
