# https://leetcode.com/problems/first-bad-version/

"""
+ To use Binary Search technique
    + If a middle element is a bad version => move to left
    + Otherwise => move to right

+ At the end, return low idx

Space complexity: O(1): 
Time complexity: O(log N): N is length of list
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 0, n

        while low <= high:
            mid = low + (high - low) // 2

            if isBadVersion(mid): # type: ignore
                high = mid - 1
            else:
                low = mid + 1

        return low