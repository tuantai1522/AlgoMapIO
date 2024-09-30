# https://leetcode.com/problems/koko-eating-bananas/description/

"""
+ To use Binary Search technique
+ At every idx mid element, count bananas monkey can eat in h hour
    + If a middle element is higher than h => return move to right
    + If a middle element is lower than h => move to left

+ At the end, return False because a target element is not in array

Space complexity: O(1): 
Time complexity: O(N * log max(piles)): N is length of list
"""

from typing import List

class Solution:
    def countBananasEatedInHHour(self, piles: List[int], h: int) -> int:
        result = 0

        for pile in piles:
            result += pile // h if pile % h == 0 else (pile // h) + 1;

        return result
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while low <= high:
            mid = low + (high - low) // 2
            count = self.countBananasEatedInHHour(piles, mid)
            if count > h:
                low = mid + 1
            else:
                high = mid - 1

        return low
        