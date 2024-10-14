# https://leetcode.com/problems/subsets/

"""
+ I am going to have 2 options: pick or not pick

+ Pick: add it to temp array and move to next position
+ Undo picking operations (remove last element)
+ Not pick: 
    
Space complexity: O(N): N is length of array
Time complexity: O(2 ^ N): is length of array
"""
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = []

        def helper(idx: int):
            if idx == len(nums):
                # I don't want a solution, I want a copy of current array
                result.append(temp[:])
                return

            # Pick current element
            temp.append(nums[idx])
            helper(idx + 1)

            # Not Pick current element
            temp.pop() # Undo adding operation
            helper(idx + 1)


        helper(0)

        return result
