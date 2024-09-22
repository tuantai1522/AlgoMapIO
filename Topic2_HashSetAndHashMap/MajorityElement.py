# https://leetcode.com/problems/majority-element/

"""
+ To loop every num in list nums
    + If count = 0 => change to new element and count it frequency in array is 1
    + Othwewise 
        => if current element equals ans => plus 1 count
        => Otherwise => minus 1 count

Space complexity: O(1):
Time complexity: O(N): N is length of list nums
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = -1
        count = 0

        for num in nums:
            if count == 0:
                ans = num
                count = 1
            else:
                if ans == num:
                    count += 1
                else:
                    count -= 1

        
        return ans