def next_char(word, idx):
    backspace_count = 0
    while idx >= 0 and (word[idx] == "<" or backspace_count > 0):
        backspace_count += 1 if word[idx] == "<" else -1
        idx -= 1

    return idx

def is_same_output(str1, str2):
    i = next_char(str1, len(str1) - 1)
    j = next_char(str2, len(str2) - 1)

    while i >= 0 and j >= 0:
        if str1[i] != str2[j]:
            return False

        i = next_char(str1, i-1)
        j = next_char(str2, j-1)

    return i == j



# True
print(is_same_output("world", "<<worrr<<ld"))
print(is_same_output("", "<<wr<<"))
print(is_same_output("w<<i", "c<<irrr<<ld<<<"))
print(is_same_output("", ""))
print(is_same_output("", "a<<"))
print(is_same_output("", "<<<"))

print()
# False
print(is_same_output("<<<", "<<worrr<<ld"))
print(is_same_output("w<<i", "c<<irrr<<ldd<<<"))


'''
Notes
* if you ask to jump into a solution, they may let you or ask for improvement
    * more likely to ask for improvement on an onsite
* have consistent spacing
    * maybe make a 4 space macro button?
* making a test suite is a better use of time if you want to write the invocation part
* know how to use a deque
* other python data structs to know
* you need to have a better idea of what you're implementing before you go for it


'''