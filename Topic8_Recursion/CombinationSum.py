# https://leetcode.com/problems/combination-sum/

"""
+ I am going to loop from the beginning of array until the end
+ I am going to have 2 options: pick or not pick

+ Base case:
    + Current sum is less than target -> don't add into result
    + Current sum equals target -> add into result
+ Pick: 
    + Add it to temp array
    + Continue to iterate at that position (allow to pick multiple times)


+ Not pick: 
    + Undo picking operations (remove last element)
    
Space complexity: O(2 ^ K): K is target sum
Time complexity: O(N): N is stored in call stack
"""


from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        temp = []
        n = len(candidates)

        def helper(idx: int, target: int):
            if target < 0:
                return

            if target == 0:
                result.append(temp[:])
                return

            for i in range(idx, n):
                temp.append(candidates[i])

                helper(i, target - candidates[i])

                temp.pop()

        helper(0, target)
        return result