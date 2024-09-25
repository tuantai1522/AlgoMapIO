# https://leetcode.com/problems/valid-parentheses

"""
+ If char is in '({[' => add it to stack
+ Otherwise, check current bracket is suitable with bracket in top element of stack or not

+ Otherwise => add integer into stack

Space complexity: O(N): N is length of str
Time complexity: O(N): N is length of str
"""
class Solution:
    def isValid(self, str: str) -> bool:
        stack = []

        for s in str:
            if s in "({[":
                stack.append(s)
            else:
                if len(stack) == 0:
                    return False
                
                temp = stack.pop()
                if (temp == '(' and s != ')') or (temp == '{' and s != '}') or (temp == '[' and s != ']'):
                    return False

        return len(stack) == 0