# https://leetcode.com/problems/reverse-string

"""
+ Using 2 pointers
    + First at the beginning
    + Second at the end

+ Swap element at idx left and idx right
    + Increase idx left
    + Decrease idx right

Space complexity: O(N): N is length of string
Time complexity: O(1): 
"""

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0 
        right = len(s) - 1

        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        