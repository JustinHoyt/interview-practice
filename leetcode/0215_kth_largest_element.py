from heapq import heappop, heappush

def kth_largest_element(nums, k):
    min_heap = []
    for num in nums:
        heappush(min_heap, num)
        if len(min_heap) == k + 1:
            heappop(min_heap)

    return heappop(min_heap)

input = [3,2,1,5,6,4]
print(kth_largest_element(input, 3))


