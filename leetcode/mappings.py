def permutations(digits, mapping, idx):
    if idx == len(digits):
        return ['']
    results = []
    for word in permutations(digits, mapping, idx + 1):
        for letter in mapping[digits[idx]]:
            results.append(letter + word)
    return results


def phone_number_to_string(digits, mapping):
    return permutations(digits, mapping, 0)


def phone_num(digits, mapping):
    if len(digits) == 0:
        return ['']
    else:
        result = []
        for sofar in phone_num(digits[1:], mapping):
            for letter in mapping[digits[0]]:
                result.append(letter + sofar)
        return result


d = {'1': ['A', 'B', 'C'], '2': ['D', 'E', 'F'], '3': ['G', 'H', 'I'], '4': ['J', 'K', 'L']}
print(phone_num("12", d))
print(phone_number_to_string("12", d))












def phone_permute_list(digits, mapping):
    if len(digits) == 0:
        return ['']
    else:
        result = []
        for x in phone_permute_list(digits[1:], mapping):
            for y in mapping[digits[0]]:
                result.append(y + x)
        return result
