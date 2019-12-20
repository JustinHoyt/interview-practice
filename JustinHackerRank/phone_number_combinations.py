# def phone_permute_list(digits, mapping):
#     if len(digits) == 0:
#         return ['']

#     result = []
#     for sofar in phone_permute_list(digits[1:], mapping):
#         for char in mapping[digits[0]]:
#             result.append(char + sofar)
#     return result


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
