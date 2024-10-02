# https://leetcode.com/problems/search-in-rotated-sorted-array

"""
+ To use Binary Search technique
    + If a middle element is a founded element => return idx
    + If a left array is sorted
        + If target in is range of left sorted array => move to left
        + Otherwise => move to right
    + Else a right array is definitely sorted
        + If target in is range of right sorted array => move to right
        + Otherwise => move to left

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
            elif nums[low] <= nums[mid]:
                if nums[low] <= target and target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            else:
                if nums[mid] <= target and target <= nums[high]:
                    low = mid + 1  
                else:
                    high = mid - 1

        return -1

