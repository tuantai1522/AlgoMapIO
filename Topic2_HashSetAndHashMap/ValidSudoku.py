# https://leetcode.com/problems/valid-sudoku/

"""
+ First step: To check every column is valid or not
+ Second step: To check every row is valid or not
+ Third step: To check every box is valid or not
    + By using array storing idx start of every box

Space complexity: O(N): N is length of list
Time complexity: O(N * M): N is length of list, M is length of every string
"""

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for i in range(0, 9):
            set_t = set()
            for j in range(0, 9):
                if board[i][j] in set_t:
                    return False

                if board[i][j] != ".":
                    set_t.add(board[i][j])

        # check column
        for i in range(0, 9):
            set_t = set()
            for j in range(0, 9):
                if board[j][i] in set_t:
                    return False

                if board[j][i] != ".":
                    set_t.add(board[j][i])

        # check box
        starts = [[0, 0], [0, 3], [0, 6],[3, 0], [3, 3], [3, 6],[6, 0], [6, 3], [6, 6]]

        for i, j in starts:
            set_t = set()
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    if board[row][col] in set_t:
                        return False

                    if board[row][col] != ".":
                        set_t.add(board[row][col])

        return True