# https://leetcode.com/problems/combinations

"""
+ I am going to loop from the beginning of array until the end
+ I am going to have 2 options: pick or not pick

+ Base case:
    Length of temp array equals to k
+ Pick: 
    + Add it to temp array
    + Move to next position

+ Not pick: 
    + Undo picking operations (remove last element)
    
Space complexity: O(N choose K): N is length of array
Time complexity: O(N): N is stored in call stack
"""

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        temp = []

        def helper(idx: int):
            if len(temp) == k:
                result.append(temp[:])
                return

            for i in range(idx, n + 1):
                temp.append(i)

                helper(i + 1)

                temp.pop()

        helper(1)
        return result