from itertools import combinations, permutations
from operator import add, mul


def test_itertools():
    # combinations
    assert list(combinations([1,2,3,4], 2)) == [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

    assert (list(permutations([1,2,3,4])) == [
        (1, 2, 3, 4),
        (1, 2, 4, 3),
        (1, 3, 2, 4),
        (1, 3, 4, 2),
        (1, 4, 2, 3),
        (1, 4, 3, 2),
        (2, 1, 3, 4),
        (2, 1, 4, 3),
        (2, 3, 1, 4),
        (2, 3, 4, 1),
        (2, 4, 1, 3),
        (2, 4, 3, 1),
        (3, 1, 2, 4),
        (3, 1, 4, 2),
        (3, 2, 1, 4),
        (3, 2, 4, 1),
        (3, 4, 1, 2),
        (3, 4, 2, 1),
        (4, 1, 2, 3),
        (4, 1, 3, 2),
        (4, 2, 1, 3),
        (4, 2, 3, 1),
        (4, 3, 1, 2),
        (4, 3, 2, 1)])


if __name__ == "__main__":
    test_itertools()
