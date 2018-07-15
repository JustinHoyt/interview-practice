
def is_valid(word):
    mymap = {}
    for char in word:
        if char in mymap:
            mymap[char] = mymap[char] + 1
        else:
            mymap[char] = 1

    occurances_map = set()
    for key in mymap:
        occurances_map[mymap[key]] = key
        # occurances_map.add(mymap[key])

    if len(occurances_map) == 1:
        return "YES"
    elif len(occurances_map) == 2:
        vals = []
        for occurances in occurances_map:
            vals.append(occurances)
        if abs(vals[0] - vals[1]) == 1:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"

test_word ="aabbcd"
print(is_valid(test_word))
