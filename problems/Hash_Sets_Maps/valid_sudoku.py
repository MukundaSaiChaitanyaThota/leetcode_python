# LeetCode Problem: Valid Sudoku
# Provided a board, determine if it is a valid Sudoku configuration.
# A valid Sudoku board (partially filled) must satisfy the following rules:
from typing import List
# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.




def isValidSudoku(board: List[List[str]]) -> bool:
    # rows
    for i in range(9): 
        unique=set()
        for j in range(9):
            item = board[i][j]
            if item in unique:
                return False
            elif item != ".":
                unique.add(item)
    # columns
    for i in range(9): 
        unique=set()
        for j in range(9):
            item = board[j][i]
            if item in unique:
                return False
            elif item != ".":
                unique.add(item)
    # 3x3 boxes
    starts = [(0,0),(0,3),(0,6),
                (3,0),(3,3),(3,6),
                (6,0),(6,3),(6,6)]

    for i,j in starts:
        unique=set()
        for p in range(i,i+3): 
            for q in range(j,j+3):
                item = board[p][q]
                if item in unique:
                    return False
                elif item != ".":
                    unique.add(item) 
    return True

if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    print(isValidSudoku(board))  # Output: True