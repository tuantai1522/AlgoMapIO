# https://leetcode.com/problems/generate-parentheses

"""
+ I am going to add open parenthesis until it doesn't satisfy conditions
(I can add more open parenthesis and a number of open parenthesis
is smaller than closed parenthesis)

+ If a number of closed and open parenthesis are 0 => add it to result

Space complexity: O(N): N is length of n storing in call stack
Time complexity: O(2 ^ N): 
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def helper(open: int, closed: int, temp: str):
            if open == 0 and closed == 0:
                result.append(temp)
                return

            if open >= 0 and open <= closed:
                temp += '('
                helper(open - 1, closed, temp)

                temp = temp[:-1]
                
                temp += ')'
                helper(open, closed - 1, temp)


        helper(n, n, "")

        return result