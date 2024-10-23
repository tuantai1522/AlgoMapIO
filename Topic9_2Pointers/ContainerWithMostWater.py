# https://leetcode.com/problems/container-with-most-water

"""
+ Using 2 pointers
    + First at the beginning
    + Second: at the end

+ I always want to move to bigger element to get the maximum area
+ At 2 idxes
    => Count area
    => Compare elements at idxes
        => If left element is bigger => decrease right pointer
        => Otherwise => increase left pointer

Space complexity: O(N): N is length of array
Time complexity: O(1): 
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        left = 0
        right = n - 1

        result = 0
        while left < right:
            x = (right - left)
            y = min(height[left], height[right])

            area = x * y

            result = max(result, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result