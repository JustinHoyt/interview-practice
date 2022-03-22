class Solution:
    def removeOnes(self, grid: list[list[int]]) -> bool:
        pattern = grid[0]
        flip_pattern = [abs(digit-1) for digit in grid[0]]
        return all((row in (pattern, flip_pattern) for row in grid))


def test_happy_path():
    assert Solution().removeOnes([
        [0,1,0],
        [1,0,1],
        [0,1,0],
    ]) == True

    assert Solution().removeOnes([
        [1,0],
        [1,0],
        [0,1],
        [0,1],
        [0,1]
    ]) == True


def test_false_case():
    assert Solution().removeOnes([
        [1,1,0],
        [1,0,1],
        [0,1,0],
    ]) == False


def test_single_cell():
    assert Solution().removeOnes([
        [0],
    ]) == True


def test_single_row():
    assert Solution().removeOnes([
        [0,1,1,0],
    ]) == True


def test_single_col():
    assert Solution().removeOnes([
        [0],
        [1],
        [1],
    ]) == True

if __name__ == "__main__":
    test_happy_path()

