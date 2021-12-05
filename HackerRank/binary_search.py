class Solution:
    def search(self, nums, target):
        left_idx = 0
        right_idx = len(nums) - 1

        while left_idx <= right_idx:
            mid_idx = (right_idx - left_idx) // 2 + left_idx
            if nums[mid_idx] == target:
                return mid_idx
            elif nums[mid_idx] < target:
                left_idx = mid_idx + 1
            else:
                right_idx = mid_idx - 1
        
        return -1

    def search_generic(self, nums, target):
        left_idx = 0
        right_idx = len(nums) - 1

        while left_idx + 1 < right_idx:
            mid_idx = (right_idx - left_idx) // 2 + left_idx
            if nums[mid_idx] == target:
                return mid_idx
            elif nums[mid_idx] < target:
                left_idx = mid_idx
            else:
                right_idx = mid_idx
        
        if nums[left_idx] == target: return left_idx
        if nums[right_idx] == target: return right_idx
        return -1



def test_happy_path():
    assert Solution().search([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 45], 43) == 11
    assert Solution().search_generic([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 45], 43) == 11

def test_end_case():
    assert Solution().search([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 45], 45) == 12
    assert Solution().search_generic([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 45], 45) == 12

def test_start_case():
    assert Solution().search([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 45], 1) == 0
    assert Solution().search_generic([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 45], 1) == 0

def test_not_found():
    assert Solution().search([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 45], 33) == -1
    assert Solution().search_generic([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 45], 33) == -1

if __name__ == "__main__":
    test_end_case()
