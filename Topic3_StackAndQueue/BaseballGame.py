# https://leetcode.com/problems/baseball-game/

"""
+ If char is 'C' => remove the last element
+ If char is '+' => add value by plusing 2 last elements
+ If char is 'D' => doubling last element
+ Otherwise => add integer into stack

Space complexity: O(N): N is length of operations
Time complexity: O(N): N is length of operations
"""

from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []

        for operation in operations:
            if operation == 'C':
                s.pop()
            elif operation == '+':
                s.append(s[-1] + s[-2])
            elif operation == 'D':
                s.append(s[-1] * 2)
            else:
                s.append(int(operation))

        return sum(s)