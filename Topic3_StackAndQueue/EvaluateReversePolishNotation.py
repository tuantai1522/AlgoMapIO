# https://leetcode.com/problems/evaluate-reverse-polish-notation

"""
+ If char is in '+-*/' => to calculate operation
+ Otherwise => add integer into stack

Space complexity: O(N): N is length of tokens
Time complexity: O(N): N is length of tokens
"""
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []

        for token in tokens:
            if token in "+-*/":
                val2, val1 = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(val1 + val2)
                elif token == '-':
                    stack.append(val1 - val2)
                elif token == '*':
                    stack.append(val1 * val2)
                else:
                    stack.append(int(val1 / val2))
            else:
                stack.append(int(token))


        return stack[0]