from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.points_count: defaultdict[tuple[int, int], int] = defaultdict(int)


    def add(self, point: list[int]) -> None:
        self.points_count[tuple(point)] += 1


    def count(self, point: list[int]) -> int:
        row, col = point
        count = 0
        for (_row, _col), _count in self.points_count.items():
            if (abs(row - _row) == abs(col - _col)        # check that it's a diagonal point
                    and (row, _col) in self.points_count  # check horizontal point exists
                    and (_row, col) in self.points_count  # check vertical point exists
                    and abs(row - _row) != 0              # check the square has an area > 0
                    ):
                # This is calculating the number of combinations for a particular square
                count += self.points_count[(row, _col)] * self.points_count[(_row, col)] * _count

        return count


def test_happy_path():
    grid = DetectSquares()
    grid.add([4,2])
    grid.add([2,4])
    grid.add([2,2])
    assert grid.count([4,4]) == 1
    grid.add([2,4])
    assert grid.count([4,4]) == 2
    grid.add([2,2])
    assert grid.count([4,4]) == 4

if __name__ == "__main__":
    test_happy_path()

