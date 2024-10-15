# https://leetcode.com/problems/permutations

"""
+ I am going to loop from the beginning of array until the end
+ I am going to have 2 options: pick or not pick

+ Pick: 
    + Add it to temp array
    + Mark it it visited array
+ Move to next position

+ Not pick: 
    + Undo picking operations (remove last element and mark as that position as not visited)
    
Space complexity: O(N): N is length of array
Time complexity: O(N ^ 2): N is stored in call stack and N is length of visited array
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = []
        n = len(nums)
        visited = [0] * n

        def helper(idx: int, visited: List[int]):
            if idx == n:
                result.append(temp[:])
                return

            for i in range(0, n):
                if visited[i] == 0:
                    # Pick
                    visited[i] = 1
                    temp.append(nums[i])

                    helper(idx + 1, visited[:])

                    # Not Pick
                    visited[i] = 0
                    temp.pop()

        helper(0, visited)
        return result