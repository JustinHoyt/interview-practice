from typing import List
from timeit import Timer

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def find_non_surrounded_regions(i, j):
            if(0 <= i < len(board)
               and 0 <= j < len(board[i])
               and board[i][j] == "O"):
                board[i][j] = "G"
                for i_offset, j_offset in directions:
                    find_non_surrounded_regions(i + i_offset, j + j_offset)

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if(i == 0
                   or i == len(board) - 1
                   or j == 0
                   or j == len(row) - 1):
                    find_non_surrounded_regions(i, j)

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if(cell == "O"):
                    board[i][j] = "X"
                elif(cell == "G"):
                    board[i][j] = "O"


board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]

print(Timer(lambda: Solution().solve(board)).timeit(number=100))
print(board)