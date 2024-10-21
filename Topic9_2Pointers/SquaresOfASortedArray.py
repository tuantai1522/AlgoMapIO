# https://leetcode.com/problems/squares-of-a-sorted-array/

"""
+ Using 2 pointers
    + First at the beginning
    + Second at the end

+ To compare value of 2 elements (ignoring plus or substract)

+ To get the bigger value and add it to result array

+ Reverse result array

Space complexity: O(N): N is length of string
Time complexity: O(1): 
"""

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0 
        right = len(nums) - 1

        result = []

        while left <= right:
            if abs(nums[left]) <= abs(nums[right]):
                result.append(nums[right] ** 2)
                right -= 1
            else:
                result.append(nums[left] ** 2)
                left += 1

        result.reverse()
        return result