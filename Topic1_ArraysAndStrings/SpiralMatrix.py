#https://leetcode.com/problems/spiral-matrix

"""
+ To traverse from left to right
+ To traverse from top to bottom
+ To traverse from right to left
+ To traverse from bottom to top

+ To multiple 2 arrays together
Space complexity: O(1)
Time complexity: O(N * N)
"""

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix or not matrix[0]:
            return result
        
        m = len(matrix)
        n = len(matrix[0])
        TOP = 0
        LEFT = 0
        RIGHT = n - 1
        BOTTOM = m - 1
        total_elements = m * n  
        value = 0  

        while value < total_elements:
            for idx in range(LEFT, RIGHT + 1):
                result.append(matrix[TOP][idx])
                value += 1
            if value >= total_elements:
                break
            TOP += 1

            for idx in range(TOP, BOTTOM + 1):
                result.append(matrix[idx][RIGHT])
                value += 1
            if value >= total_elements:
                break
            RIGHT -= 1

            for idx in range(RIGHT, LEFT - 1, -1):
                result.append(matrix[BOTTOM][idx])
                value += 1
            if value >= total_elements:
                break
            BOTTOM -= 1

            for idx in range(BOTTOM, TOP - 1, -1):
                result.append(matrix[idx][LEFT])
                value += 1
            if value >= total_elements:
                break
            LEFT += 1

        return result
