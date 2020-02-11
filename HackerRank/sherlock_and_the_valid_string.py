# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
class valid_string:
def is_valid(self, word):
    mymap = {}
    for char in word:
        if char in mymap:
            mymap[char] = mymap[char] + 1
        else:
            mymap[char] = 1

    occurances_map = {}
    for key in mymap:
        if mymap[key] in occurances_map:
            occurances_map[mymap[key]] = occurances_map[mymap[key]] + key
        else:
            occurances_map[mymap[key]] = key

    if len(occurances_map) == 1:
        return "YES"
    elif len(occurances_map) == 2:
        if 1 in occurances_map and len(occurances_map[1]) == 1:
            return "YES"
        occurances = []
        for num_occurances in occurances_map:
            occurances.append(num_occurances)
            occurances.sort()
        if occurances[1] - occurances[0] == 1:
            if len(occurances_map[occurances[1]]) == 1 and len(occurances_map[occurances[0]]) > 1:
                return "YES"
            else:
                return "NO"
        else:
            return "NO"
    else:
        return "NO"
