from operator import lt, le

class Solution:
    def search_left(self, nums, target):
        low = 0
        high = len(nums)

        while low < high:
            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        return low if nums[low] == target else -1

    def search_right(self, nums, target):
        low = 0
        high = len(nums)

        while low < high:
            mid = (low + high) // 2

            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid

        return low - 1 if nums[low - 1] == target else -1

    def search(self, nums, target, direction='left'):
        low = 0
        high = len(nums)

        comparator = lt if direction == 'left' else le

        while lt(low,high):
            mid = (low + high) // 2

            if comparator(nums[mid], target):
                low = mid + 1
            else:
                high = mid

        idx = low if direction == 'left' else low - 1
        return idx if nums[idx] == target else -1



def test_happy_path():
    assert Solution().search_left([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 45], 43) == 11
    assert Solution().search_right([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 45], 43) == 11
    assert Solution().search([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 45], 43) == 11

def test_end_case():
    assert Solution().search_left([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 45], 45) == 12
    assert Solution().search_right([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 45], 45) == 12
    assert Solution().search([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 45], 45, 'right') == 12

def test_start_case():
    assert Solution().search_left([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 45], 1) == 0
    assert Solution().search_right([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 45], 1) == 0
    assert Solution().search([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 45], 1, 'right') == 0

def test_not_found():
    assert Solution().search_left([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 45], 33) == -1
    assert Solution().search_right([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 45], 33) == -1
    assert Solution().search([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 45], 33, 'left') == -1

def test_duplicate_case():
    assert Solution().search_left([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 43, 45], 43) == 11
    assert Solution().search_right([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 43, 45], 43) == 12
    assert Solution().search([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 43, 45], 43, 'left') == 11
    assert Solution().search([1, 3, 4, 5, 6, 7, 9, 10, 11, 20, 30, 43, 43, 45], 43, 'right') == 12

if __name__ == "__main__":
    test_end_case()
