from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_digit_count = Counter(secret)
        guess_digit_count = Counter(guess)

        matches = 0
        exact_matches = 0
        for guess_digit, count in guess_digit_count.items():
            if guess_digit in secret_digit_count:
                matches += min(count, secret_digit_count[guess_digit])

        for guess_digit, secret_digit in zip(guess, secret):
            if guess_digit == secret_digit:
                exact_matches += 1

        return f'{exact_matches}A{matches - exact_matches}B'



def test_happy_path():
    assert Solution().getHint('1807',
                              '7810') == '1A3B'

    assert Solution().getHint('1123',
                              '0111') == '1A1B'

if __name__ == "__main__":
    test_happy_path()

