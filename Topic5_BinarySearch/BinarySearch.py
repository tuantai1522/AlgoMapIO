# https://leetcode.com/problems/binary-search/description/

"""
+ To use Binary Search technique
    + If a middle element is a founded element => return idx
    + If a middle element is higher than a founded element => move to left
    + Otherwise => move to right

+ At the end, return -1 because a target element is not in array

Space complexity: O(1): 
Time complexity: O(log N): N is length of list
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1