from typing import *

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results: List[List[int]] = []
        def subsets_rec(sofar: List[int], idx: int):
            if idx == len(nums):
                results.append(sofar)
                return
            
            subsets_rec(sofar.copy(), idx + 1)
            sofar.append(nums[idx])
            subsets_rec(sofar.copy(), idx + 1)

        subsets_rec([], 0)
        print(results)
        return results


def test_happy_path():
    assert Solution().subsets([1,2,3]) == [[],[3],[2],[2,3],[1],[1,3],[1,2],[1,2,3]]

def test_single_element():
    assert Solution().subsets([0]) == [[],[0]]

def test_empty_list():
    assert Solution().subsets([]) == [[]]

if __name__ == "__main__":
    test_happy_path()