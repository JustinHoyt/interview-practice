def min_swaps_to_anagram(str1, str2):
    min_swaps = 0
    char_map = {}
    for char in str1:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1

    for char in str2:
        if char in char_map and char_map[char] > 0:
            char_map[char] -= 1

    for count in char_map.values():
        min_swaps += count

    return min_swaps


input_10, input_11 = ('abcdeee', 'ecdeeba')
input_20, input_21 = ('a', 'b')
input_30, input_31 = ('', '')
input_40, input_41 = ('aaaa', 'aaaa')
input_50, input_51 = ('xaxb', 'bbxx')

print(min_swaps_to_anagram(input_10, input_11), 0)
print(min_swaps_to_anagram(input_20, input_21), 1)
print(min_swaps_to_anagram(input_30, input_31), 0)
print(min_swaps_to_anagram(input_40, input_41), 0)
print(min_swaps_to_anagram(input_50, input_51), 1)
