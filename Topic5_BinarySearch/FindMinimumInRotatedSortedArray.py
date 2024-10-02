# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

"""
+ To use Binary Search technique
    + If a left array is sorted
        + Get the minimum element at left idx
        + Move to right
    + Else a right array is definitely sorted
        + Get the minimum element at mid idx
        + Move to left

+ At the end, return -1 because a target element is not in array

Space complexity: O(1): 
Time complexity: O(log N): N is length of list
"""

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        mini = float("inf")

        while low <= high:
            mid = low + (high - low) // 2

            if nums[low] <= nums[mid]:
                mini = min(nums[low], mini)
                low = mid + 1
            else:
                mini = min(nums[mid], mini)
                high = mid - 1

        return mini 