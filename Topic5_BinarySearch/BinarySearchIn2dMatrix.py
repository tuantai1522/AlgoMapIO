# https://leetcode.com/problems/search-a-2d-matrix/

"""
+ To use Binary Search technique
+ Suitable idx: [mid / c][mid % c] (c is column of matrix)
    + If a middle element is a founded element => return True
    + If a middle element is higher than a founded element => move to left
    + Otherwise => move to right

+ At the end, return False because a target element is not in array

Space complexity: O(1): 
Time complexity: O(log N * M): N is row and M is column
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) * len(matrix[0]) - 1

        while low <= high:
            mid = low + (high - low) // 2
            val = matrix[mid // len(matrix[0])][mid % len(matrix[0])]

            if val == target:
                return True
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1


        return False