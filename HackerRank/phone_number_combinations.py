def phone_permute_list(digits, mapping, i = 0):
    if i == len(digits):
        return ['']

    results = []
    for result_sofar in phone_permute_list(digits, mapping, i + 1):
        for char in mapping[digits[i]]:
            results.append(char + result_sofar)
    return results


mapping = {'1': ['A', 'B', 'C'], '2': ['D', 'E', 'F'], '3': ['G', 'H', 'I'], '4': ['J', 'K', 'L'] }

digits = "12"
print(phone_permute_list(digits, mapping))
