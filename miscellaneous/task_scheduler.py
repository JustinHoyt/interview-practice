# for [3,3,1,3]
# the map would look like: {3: [0,1,3], 1: [2]}
from collections import defaultdict
def min_intervals(tasks, cooldown):
    intervals = 0
    interval_map = defaultdict(list)
    for i in range(len(tasks)):
        interval_map[tasks[i]] = [i]
    for task in interval_map:
        intervals += 1
        for i in range(len(interval_map[task]) - 1):
            intervals += max(0, interval_map[task[i+1]] - interval_map[task[i]])
    return intervals


# Enter your code here. Read input from STDIN. Print output to STDOUT
# input = [3,3,1,3] c = 2
print(min_intervals([3,3,1,3],2))
