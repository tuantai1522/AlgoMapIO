# https://leetcode.com/problems/two-sum/

"""
+ To loop every num in list nums
    + If target - nums[idx] in dict => return array of idx
    + Othwewise => add it to dict with key is current element and its value is idx

Space complexity: O(N): N is length of list nums
Time complexity: O(N): N is length of list nums
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for idx in range (0, len(nums)):
            if target - nums[idx] in dict:
                return [dict[target - nums[idx]], idx]
            else:
                dict[nums[idx]] = idx
