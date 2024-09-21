# https://leetcode.com/problems/jewels-and-stones/

"""
+ First step: To build set based on ouput list
+ Second step: To check whether len of set equals len of list or not
Space complexity: O(N): N is length of list
Time complexity: O(N): N is length of list
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)

        return len(s) != len(nums)