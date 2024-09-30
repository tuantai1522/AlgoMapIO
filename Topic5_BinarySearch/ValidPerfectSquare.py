# https://leetcode.com/problems/valid-perfect-square/description/

"""
+ To use Binary Search technique
    + If a value by multiplying middle element together is integer => return true
    + If a value by multiplying middle element together is higher than num => move to left
    + Otherwise => move to right

+ At the end, return False

Space complexity: O(1): 
Time complexity: O(log N): N is length of list
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 1, num

        while low <= high:
            mid = low + (high - low) // 2
            count = mid * mid
            if count == num:
                return True;
            elif count > num:
                high = mid - 1
            else:
                low = mid + 1

        return False