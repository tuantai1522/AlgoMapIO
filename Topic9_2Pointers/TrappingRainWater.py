# https://leetcode.com/problems/trapping-rain-water/

"""
+ To build 2 array
    + First: At idx, to get the maximum value from 0 to idx - 1
    + Second: At idx, to get the maximum value from idx + 1 to n - 1

+ After that, iterate every element
    + If value is positive by plusing 2 elements and substract
current height => ignore 
    + Otherwise plus that answer to result

Space complexity: O(N): N is length of array
Time complexity: O(N): 
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n

        max_temp = height[0]
        for idx in range(1, n):
            max_left[idx] = max_temp
            max_temp = max(max_temp, height[idx])

        max_temp = height[n - 1]
        for idx in range(n - 2, -1, -1):
            max_right[idx] = max_temp
            max_temp = max(max_temp, height[idx])

        result = 0
        for idx in range(0, n):
            count = min(max_left[idx], max_right[idx]) - height[idx]

            if count > 0:
                result += count

        return result