class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def divide_rec(dividend):
            if dividend < divisor:
                return 0
            i = 0
            while (divisor << (i + 1)) < dividend:
                i += 1

            times_added = 1 << i
            return (times_added
                    + self.divide(dividend - (divisor << i), divisor))

        # To handle 32 bit signed int bound test
        if dividend == -(1 << 31) and divisor == -1:
            return (1 << 31) - 1

        is_positive = False
        if (dividend >= 0 and divisor >= 0) or (dividend < 0 and divisor < 0):
            is_positive = True

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = divide_rec(dividend)
        return result if is_positive else ~result + 1


def test_happy_path():
    assert Solution().divide(40, 3) == 13


def test_negative_number():
    assert Solution().divide(7, -3) == -2


def test_identity():
    assert Solution().divide(1, 1) == 1


def test_zero_dividend():
    assert Solution().divide(0, 100) == 0


def test_zero_dividend_negative_divisor():
    assert Solution().divide(0, -100) == 0


def test_bounds():
    assert Solution().divide(-2147483648, -1) == 2147483647


if __name__ == "__main__":
    test_happy_path()
