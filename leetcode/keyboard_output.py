def next_char(keys, i):
    num_backspaces = 0
    while keys[i] == "<" or num_backspaces > 0:
        if i < 0:
            return -1
        if keys[i] == "<":
            num_backspaces += 1
        elif num_backspaces > 0:
            num_backspaces -= 1

        i -= 1
    return i

def is_same_output(keys1, keys2):
    i = len(keys1) - 1
    j = len(keys2) - 1
    while i >= 0 or j >= 0:
        i = next_char(keys1, i)
        j = next_char(keys2, j)
        if i == -1 and j == -1:
            return True
        if i == -1 or j == -1 or keys1[i] != keys2[j]:
            return False

        i -= 1
        j -= 1

    return True


keys1 = "abc<<c"
keys2 = "a<<<c"
print(is_same_output(keys1, keys2))
assert not is_same_output(keys1, keys2)

keys1 = "abc<<c"
keys2 = "a<ac"
print(is_same_output(keys1, keys2))
assert is_same_output(keys1, keys2)

keys1 = "abc<<c"
keys2 = "ba<ac"
print(is_same_output(keys1, keys2))
assert not is_same_output(keys1, keys2)

keys1 = "<<<"
keys2 = "<"
print(is_same_output(keys1, keys2))
assert is_same_output(keys1, keys2)

keys1 = "<<ab<"
keys2 = "ab<"
print(is_same_output(keys1, keys2))
assert is_same_output(keys1, keys2)
