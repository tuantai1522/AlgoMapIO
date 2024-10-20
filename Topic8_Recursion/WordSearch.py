# https://leetcode.com/problems/word-search/

"""
+ I am going to loop every single character in board and run recursion on that character
    + First: I need to mark cell as visited if it's already iterated
    + Second: I am going to have an idx to store current element in word
and compared with current cell to see it equals or not
    + Base case:
        + Row exceeds 0 or length of rows
        + Col exceeds 0 or length of cols
        + Current cell != current character in word => False

Space complexity: O((M * N) ^ 2): M is length of row, N is length of col
Time complexity: O(L): L is length of word storing in call stack 
"""
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(idx: int, row: int, col: int, rows: int, cols: int, temp: str) -> bool:
            if idx == len(word):
                return True

            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] == '#':
                return False
            
            if board[row][col] != word[idx]:
                return False

            temp += board[row][col]

            curVal = board[row][col]
            board[row][col] = '#'

            left = helper(idx + 1, row - 1, col, rows, cols, temp)
            top = helper(idx + 1, row, col - 1, rows, cols, temp)
            right = helper(idx + 1, row, col + 1, rows, cols, temp)
            bottom = helper(idx + 1, row + 1, col, rows, cols, temp) 

            board[row][col] = curVal

            return left or top or right or bottom
            

        for row in range(0, len(board)):
            for col in range (0, len(board[0])):
                check = helper(0, row, col, len(board), len(board[0]), "")
                if check == True:
                    return True

        return False