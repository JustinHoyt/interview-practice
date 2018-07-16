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

        # print(occurances_map)
        if len(occurances_map) == 1:
            return "YES"
        elif len(occurances_map) == 2:
            vals = []
            for num_occurances in occurances_map:
                vals.append(num_occurances)
            if abs(vals[0] - vals[1]) == 1:
                if len(occurances_map[vals[0]]) > 1 and len(occurances_map[vals[1]]) > 1:
                    return "NO"
                else:
                    return "YES"
            else:
                return "NO"
        else:
            return "NO"
