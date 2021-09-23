from collections import Counter
from typing import *
from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def build_heap(freq_map: Dict[int, int]) -> List[Tuple[int, int]]:
            min_heap: List[Tuple[int, int]] = []
            for val, freq in freq_map.items():
                heappush(min_heap, (freq, val))
                if len(min_heap) > k:
                    heappop(min_heap)

            return min_heap


        freq_map = Counter(nums)
        min_heap = build_heap(freq_map)
        results = []
        for _, val in min_heap:
            results.append(val)
        
        return results


    def topKFrequentQuickSelect(self, nums: List[int], k: int) -> List[int]:
        results: List[int] = []
        freq_list = list(Counter(nums).items())

        def partition(left, right):
            nonlocal freq_list
            pivot = freq_list[right][1]
            pivot_idx = left
            for swap_idx in range(left, right):
                if freq_list[swap_idx][1] > pivot:
                    freq_list[pivot_idx], freq_list[swap_idx] = freq_list[swap_idx], freq_list[pivot_idx]
                    pivot_idx += 1
            
            freq_list[pivot_idx], freq_list[right] = freq_list[right], freq_list[pivot_idx]

            return pivot_idx

        def quickSelect(left, right):
            nonlocal freq_list
            if left >= right:
                return

            pivot_idx = partition(left, right)
            quickSelect(left, pivot_idx - 1)
            quickSelect(pivot_idx + 1, right)

        quickSelect(0, len(freq_list) - 1)

        for i in range(k):
            results.append(freq_list[i][0])
        return results


def test_happy_path():
    assert sorted(Solution().topKFrequent([1,1,1,2,2,3], 2)) == sorted([1,2])
    assert sorted(Solution().topKFrequentQuickSelect([1,1,1,2,2,3], 2)) == sorted([1,2])

def test_two_highest():
    assert sorted(Solution().topKFrequent([4,1,-1,2,-1,2,3], 2)) == sorted([-1,2])
    assert sorted(Solution().topKFrequentQuickSelect([4,1,-1,2,-1,2,3], 2)) == sorted([-1,2])

def test_one_item_recurring():
    assert sorted(Solution().topKFrequent([-1, -1], 1)) == sorted([-1])
    assert sorted(Solution().topKFrequentQuickSelect([-1, -1], 1)) == sorted([-1])

def test_single_item():
    assert sorted(Solution().topKFrequent([1], 1)) == sorted([1])
    assert sorted(Solution().topKFrequentQuickSelect([1], 1)) == sorted([1])

if __name__ == "__main__":
    test_two_highest()