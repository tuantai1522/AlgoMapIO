# https://leetcode.com/problems/maximum-average-subarray-i/

"""
+ To build total_sum range from [0, k]

+ I am going to use sliding window from [1, n - k]
    + Build range sum from [idx] to [idx + k]
        + Minusing previos element
        + Plus element at idx + k index

        + Get the maximum result by comparing that with max_sum

Time complexity: O(N): N is length of array
Space complexity: O(1)

"""
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        sum = 0
        for idx in range(0, k):
            sum += nums[idx]

        result = sum / k

        right = 1 + k - 1
        for left in range(1, n - k + 1):
            sum = (sum - nums[left - 1] + nums[right])

            result = max(result, sum / k)

            right += 1

        return result
        