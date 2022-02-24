class Solution:
    def sqrt(self, n):
        low = 0
        high = n

        while low < high:
            mid = (low + high) // 2
            if mid * mid < n:
                low = mid + 1
            else:
                high = mid

        return low if low * low == n else low - 1


def test_happy_path():
    assert Solution().sqrt(16) == 4

def test_under_by_one():
    assert Solution().sqrt(15) == 3

def test_over_by_one():
    assert Solution().sqrt(17) == 4

def test_zero_case():
    assert Solution().sqrt(0) == 0

def test_one_case():
    assert Solution().sqrt(1) == 1

def test_two_case():
    assert Solution().sqrt(2) == 1

if __name__ == "__main__":
    test_happy_path()

