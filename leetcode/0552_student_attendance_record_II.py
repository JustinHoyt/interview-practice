from itertools import combinations_with_replacement, permutations
from functools import cache
from timer import timer
import sys

sys.setrecursionlimit(1000000)

class Solution:
    @timer
    def checkRecord(self, n: int) -> int:
        mod_int = 1000000007
        base_list = [1,2,4,7]

        @cache
        def func(_n):
            if _n < len(base_list):
                return base_list[_n]

            return (2*func(_n-1) - func(_n-4)) % mod_int


        f = [func(i) for i in range(n+1)]

        return (sum(f[i-1] * f[n-i] for i in range(1, n+1)) + func(n)) % mod_int


    def checkRecordBacktracking(self, n: int) -> int:
        count = 0

        def check_record(sofar: list[str], absent_count) -> None:
            nonlocal count

            if absent_count > 1:
                return

            if len(sofar) > 2 and sofar[-1] == sofar[-2] == sofar[-3] == 'L':
                return

            if len(sofar) == n:
                count += 1
                return

            for record in 'ALP':
                sofar.append(record)
                _absent_count = absent_count + 1 if record == 'A' else absent_count
                check_record(sofar, _absent_count)
                sofar.pop()


        check_record([], 0)
        return count


    def checkRecordSlow(self, n: int) -> int:
        count = 0
        for combination in combinations_with_replacement('ALP', n):
            if combination.count('A') > 1:
                continue

            for permutation in set(permutations(combination)):
                if 'LLL' not in ''.join(permutation):
                    count += 1

        return count


def test_happy_path():
    tests = [
        (0, 1),
        (1, 3),
        (2, 8),
        (3, 19),
        (4, 43),
        (5, 94),
        (6, 200),
        (7, 418),
        (8, 861),
        (9, 1753),
        (10, 3536),
        (11, 7077),
        (12, 14071),
        (13, 27820),
        (14, 54736),
        (15, 107236),
        (16, 209305),
        (17, 407167),
        (18, 789720),
        (19, 1527607),
        (20, 2947811),
    ]
    for n, expected in tests:
        assert Solution().checkRecord(n) == expected


if __name__ == "__main__":
    test_happy_path()

