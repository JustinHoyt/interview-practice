from typing import *

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        def traverse() -> Tuple[int, List[int]]:
            direction = 0
            location = [0, 0]

            for instruction in instructions:
                if instruction == 'G':
                    if direction == 0: location[0] += 1
                    if direction == 1: location[1] += 1
                    if direction == 2: location[0] -= 1
                    if direction == 3: location[1] -= 1
                if instruction == 'R':
                    direction = (direction + 1) % 4
                if instruction == 'L':
                    direction = (direction + 3) % 4
            
            return direction, location

        direction, end_location = traverse()
        if end_location == [0, 0] or direction != 0: return True
        else: return False


def test_small_circle():
    assert Solution().isRobotBounded('GGLLGG') == True

def test_straight_line():
    assert Solution().isRobotBounded('GG') == False

def test_diagonal_line():
    assert Solution().isRobotBounded('GLGR') == False

def test_no_instructions():
    assert Solution().isRobotBounded('') == True


if __name__ == "__main__":
    test_no_instructions()