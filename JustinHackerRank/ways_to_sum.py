from collections import deque

def ways_to_sum(sum):
    sums = [1, 1, 1, 2]
    for i in range(4, sum+1):
        sums.append(sums[i-1] + sums[i-3] + sums[i-4])
    return sums[sum]


def ways_to_sum_queue(sum):
    sum_queue = deque([1,1,1,2])
    if sum < 4:
        return sum_queue[sum]
    for i in range(4, sum+1):
        sum_queue.append(sum_queue[-1] + sum_queue[-3] + sum_queue[-4])
        sum_queue.popleft()
    return sum_queue[-1]


print(ways_to_sum(6))
print(ways_to_sum_queue(4))
