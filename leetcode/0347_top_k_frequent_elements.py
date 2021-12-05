from collections import Counter
from typing import *
from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def build_heap():
            heap = []
            num_counts = Counter(nums)
            for num, freq in num_counts.items():
                heappush(heap, (freq, num))
                if len(heap) > k:
                    heappop(heap)
            return heap


        min_heap = build_heap()
        result = []
        while min_heap:
            temp = heappop(min_heap)
            result.append(temp[1])
        
        return result

    def topKFrequentQuickSelect()




def test_happy_path():
    assert sorted(Solution().topKFrequent([1,1,1,2,2,3], 2)) == sorted([1,2])
    # assert sorted(Solution().topKFrequentQuickSelect([1,1,1,2,2,3], 2)) == sorted([1,2])

def test_two_highest():
    assert sorted(Solution().topKFrequent([4,1,-1,2,-1,2,3], 2)) == sorted([-1,2])
    # assert sorted(Solution().topKFrequentQuickSelect([4,1,-1,2,-1,2,3], 2)) == sorted([-1,2])

def test_one_item_recurring():
    assert sorted(Solution().topKFrequent([-1, -1], 1)) == sorted([-1])
    # assert sorted(Solution().topKFrequentQuickSelect([-1, -1], 1)) == sorted([-1])

def test_single_item():
    assert sorted(Solution().topKFrequent([1], 1)) == sorted([1])
    # assert sorted(Solution().topKFrequentQuickSelect([1], 1)) == sorted([1])

if __name__ == "__main__":
    test_two_highest()