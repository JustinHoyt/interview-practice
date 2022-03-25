from math import sqrt
from typing import Counter


class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        num_boomerangs = 0
        for i1, j1 in points:
            dist_counter: Counter[str] = Counter()
            for i2, j2 in points:
                if i1 == i2 and j1 == j2:
                    continue

                dist = "{:.4f}".format(sqrt(abs(i1 - i2)**2 + abs(j1 - j2)**2))

                dist_counter[dist] += 1

            num_boomerangs += sum((n * (n-1) for n in dist_counter.values()))

        return num_boomerangs


def test_happy_path():
    assert Solution().numberOfBoomerangs([
        [0,0],
        [1,0],
        [2,0],
    ]) == 2


def test_diagonal():
    assert Solution().numberOfBoomerangs([
        [1,1],
        [2,2],
        [3,3],
    ]) == 2


def test_4_matches():
    assert Solution().numberOfBoomerangs([
        [1,1],
        [2,2],
        [2,3],
        [3,3],
        [3,2],
    ]) == 12

    assert Solution().numberOfBoomerangs([
        [0,0],
        [1,0],
        [-1,0],
        [0,1],
        [0,-1]
    ]) == 20


def test_no_boomerang():
    assert Solution().numberOfBoomerangs([
        [1,1],
    ]) == 0


if __name__ == "__main__":
    test_4_matches()

