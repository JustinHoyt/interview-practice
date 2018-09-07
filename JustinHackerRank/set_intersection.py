'''
Given a list of sets, find the set that should be excluded to
maximize the size of the intersection of the remaining sets
'''
def max_intersection(sets):
    size = len(sets)
    if size <= 1:
        return -1
    memo = {(0,0): sets[0]}
    for i in range(1, size):
        memo[(0,i)] = memo[(0,i-1)].intersection(sets[i])
    memo[(size-1,size-1)] = sets[size-1]
    for i in range(size-1, -1, -1):
        memo[(i-1,size-1)] = memo[(i, size-1)].intersection(sets[i-1])

    max_intersection = 0
    best_ignored_intersection = 0
    for i in range(size):
        temp_intersection = set()
        if i == 0:
            temp_intersection = memo[(1, size-1)]
        elif i == size-1:
            temp_intersection = memo[(0, size-2)]
        else:
            temp_intersection = memo[(0, i-1)].intersection(memo[(i+1, size-1)])
        if len(temp_intersection) > max_intersection:
            max_intersection = len(temp_intersection)
            best_ignored_intersection = i
    return best_ignored_intersection


sets = [{3,4,6,9},
        {3,4,6,9},
        {3,4,9,6},
        {2,3,4,5,6}
        ]

print(max_intersection(sets))


def max_intersection_brute_force(sets):
    if len(sets) <= 1:
        return -1
        # map[(0,i)] = map[(o,i-1

    max_intersection = 0
    best_ignored_intersection = 0
    for i in range(len(sets)):
        temp_intersection = set()
        if i == 0 and len(sets) > 1:
            temp_intersection = sets[1]
        else:
            temp_intersection = sets[0]
        for j in range(len(sets)):
            if j != i:
                temp_intersection = sets[j].intersection(temp_intersection)
        if len(temp_intersection) > max_intersection:
            max_intersection = len(temp_intersection)
            best_ignored_intersection = i
    return best_ignored_intersection


sets = [{1, 2, 4, 9, 3},
        {4, 9, 3},
        {4, 9, 3},
        {4, 9, 3}
        ]

print(max_intersection_brute_force(sets))
