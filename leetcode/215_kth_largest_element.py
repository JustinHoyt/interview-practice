import heapq

def kth_largest_element(nums, k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) == k + 1:
            heapq.heappop(min_heap)
    print(min_heap)
    return heapq.heappop(min_heap)

input = [3,2,1,5,6,4]
print(kth_largest_element(input, 3))


