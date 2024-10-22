# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

"""
+ Using 2 pointers
    + First at the beginning
    + Second at the end

+ Count current sum by plusing 2 elements at 2 idxes
+ If it equals target => return
+ If it's smaller than target => increase left pointer
+ Otherwise, decrease right pointer

Space complexity: O(N): N is length of array
Time complexity: O(1): 
"""
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        left = 0
        right = n - 1

        while left < right:
            cur_sum = numbers[left] + numbers[right]

            if cur_sum == target:
                return [left + 1, right + 1]
            elif cur_sum < target:
                left += 1
            else:
                right -= 1

        return []