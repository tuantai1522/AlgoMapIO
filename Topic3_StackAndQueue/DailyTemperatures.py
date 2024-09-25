# https://leetcode.com/problems/daily-temperatures

"""
+ Using monotomic stack
    + stack is always increasing
    + If current value is higher than the top element of stack => place it into right place in stack

Space complexity: O(N): N is length of temperatures
Time complexity: O(N): N is length of temperatures
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for idx in range(0, len(temperatures)):
            while(len(stack) != 0 and temperatures[idx] > stack[-1][0]):
                temp = stack.pop()
                result[temp[1]] = idx - temp[1]

            stack.append([temperatures[idx], idx])

        return result