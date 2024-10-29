# https://leetcode.com/problems/minimum-size-subarray-sum/
"""
+ I am going to have 2 pointers: left and right
    + Left at the beginning
    + Right for iteration

+ Range [left, right] is always invalid (smaller than target)
    + If it's valid => move left pointer to make it invalid
    + Count range when moving left pointer

Time complexity: O(N): N is length of array
Space complexity: O(1):
"""

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_sum = 0
        n = len(nums)
        left = 0    
        result = float("inf")

        for right in range(0, n):        
            if nums[right] == target:
                return 1
            
            cur_sum += nums[right]
            if cur_sum >= target:
                while left < n and cur_sum >= target:
                    result = min(result, right - left + 1)
                    cur_sum -= nums[left]

                    left += 1

        return result if result != float("inf") else 0