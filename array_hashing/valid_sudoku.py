# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according
# to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Create a set for row, column, and square
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        # for each row
        for r in range(9):
            # for each column
            for c in range(9):
                
                # if the current board space is empty, continue
                if board[r][c] == ".":
                    continue
                
                # if the current board value is in the current row
                # of the current board value is in the current column
                if (board[r][c] in row[r] or

                    board[r][c] in col[c] or
                    board[r][c] in square[(r//3, c//3)]):
                    return False
                
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c]) 
                
        return True


# Test Cases
sol = Solution()

board1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(sol.isValidSudoku(board1))
print(sol.isValidSudoku(board2))