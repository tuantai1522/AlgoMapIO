# https://leetcode.com/problems/rotate-image

"""
+ First step: To swap value of [row, column] into [column, row]
+ Second step: We will swap values between 2 columns (first_col and end_col) until it meets 
Space complexity: O(1)
Time complexity: O(N * N)
"""

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Swap [row, col] => [col,row]
        n = len(matrix)

        for i in range (0, n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        first_col = 0
        end_col = n - 1
        while first_col < end_col:
            for i in range (0, n):
                matrix[i][first_col], matrix[i][end_col] = matrix[i][end_col], matrix[i][first_col]
            
            first_col += 1
            end_col -= 1
