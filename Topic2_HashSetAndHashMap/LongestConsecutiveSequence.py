# https://leetcode.com/problems/longest-consecutive-sequence/

"""
+ First step: To build set based on nums
+ Second step: To check if current value minuses 1 is in set or not
    + If not => current value is a start of sequence => iterate
    + Otherwise => current value is in the sequence => ignore
Space complexity: O(N): N is length of nums
Time complexity: O(N): N is length of nums
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_t = set(nums)

        result = 0

        for num in nums:
            if(num - 1) not in set_t:
                temp = num
                count = 0
                while temp in set_t:
                    count += 1
                    temp += 1

                result = max(result, count)

        return result
