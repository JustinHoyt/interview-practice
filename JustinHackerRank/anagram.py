def min_changes_to_anagram(str1, str2):
    min_changes = 0
    letter_frequency_map = {}
    for letter in str1:
        if letter in char_map:
            letter_frequency_map[char] += 1
        else:
            letter_frequency_map[char] = 1

    for letter in str2:
        if letter in char_map and char_map[char] > 0:
            letter_frequency_map[char] -= 1

    for count in letter_frequency_map.values():
        min_changes += count

    return min_changes


input_10, input_11 = ('abcdeee', 'ecdeeba')
input_20, input_21 = ('a', 'b')
input_30, input_31 = ('', '')
input_40, input_41 = ('aaaa', 'aaaa')
input_50, input_51 = ('xaxb', 'bbxx')

print(min_changes_to_anagram(input_10, input_11), 0)
print(min_changes_to_anagram(input_20, input_21), 1)
print(min_changes_to_anagram(input_30, input_31), 0)
print(min_changes_to_anagram(input_40, input_41), 0)
print(min_changes_to_anagram(input_50, input_51), 1)
