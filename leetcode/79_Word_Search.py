class Solution:
    def exist(self, board, word):
        # a visited map keeps our input in tact at the cost of space.
        visited = {}

        # simpler argument list from nested function.
        def getWords(i, j, pos = 0):
            # simipler base case by looking for the out of bounds case.
            if pos == len(word):
                return True

            # the inclusive case is easier to write and read than the exclusive case in this instance.
            # new lines help make long if-statements more readable.
            if (0 <= i < len(board) and 
                    0 <= j < len(board[0]) and 
                    not visited.get((i, j)) and 
                    word[pos] == board[i][j]):
                visited[(i, j)] = True

                res = False
                # an on the fly array of offsets reduces code duplication.
                for i_offset, j_offset in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    # the or-equals operator makes more succinct code.
                    res |= getWords(i + i_offset, j + j_offset, pos + 1)
                visited[(i, j)] = False

                return res

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if getWords(i, j):
                    return True
        
        return False


board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"

print(Solution().exist(board, word))
