# https://leetcode.com/problems/max-consecutive-ones-iii/

"""
+ To build range from [left, right] which is in range of valid 0

+ Two pointers: left, and right at the beginning
    + Left at the beginning
    + Right for iteration

+ If I see 0 value in array
    => plus count_zero variable one value
    => Move left pointer to valid idx where range [left, right]
contains only k 0 elements

Time complexity: O(N): N is length of array
Space complexity: O(1)
"""
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)

        max_consecutive = 0
        num_zeros = 0
        left = 0

        for right in range(n):
            if nums[right] == 0:
                num_zeros += 1
                while num_zeros > k:
                    if nums[left] == 0:
                        num_zeros -= 1
                    left += 1

            max_consecutive = max(max_consecutive, right - left + 1)

        return max_consecutive