class Solution:
    def combine(self, n: int, k: int):
        combinations = []
        def generate_combinations(idx: int, sofar: list[int]):
            if len(sofar) == k:
                combinations.append(sofar[:])
                return
            if idx > n:
                return

            generate_combinations(idx + 1, sofar)
            sofar.append(idx)
            generate_combinations(idx + 1, sofar)
            sofar.pop()

        generate_combinations(1, [])
        return combinations


    def combine_built_in(self, n: int, k: int):
        from itertools import combinations
        return combinations(list(range(1,n+1)), k)


def test_happy_path():
    assert sorted(Solution().combine(4, 2)) == sorted([
        [2,4],
        [3,4],
        [2,3],
        [1,2],
        [1,3],
        [1,4],
    ])
    assert sorted(Solution().combine_built_in(4, 2)) == sorted([
        (2,4),
        (3,4),
        (2,3),
        (1,2),
        (1,3),
        (1,4),
    ])


if __name__ == "__main__":
    test_happy_path()

