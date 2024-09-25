# https://leetcode.com/problems/min-stack/

"""
+ I am going to store 2 stacks
+ First stack as normal => push, pop
+ Second stack is min stack
    + Always compare value which I am going to added with top value => get Min and add to min Stack array

Space complexity: O(N ^ 2): N is a number of elements pushed into stack
Time complexity: O(1): 
"""

class MinStack:
    def __init__(self):
        self.stack_1 = []  
        self.stack_2 = []  

    def push(self, val: int) -> None:
        self.stack_1.append(val)
        self.stack_2.append(min(val, val if len(self.stack_2) == 0 else self.stack_2[-1]))

    def pop(self) -> None:
        self.stack_1.pop()
        self.stack_2.pop()

    def top(self) -> int:
        return self.stack_1[-1]

    def getMin(self) -> int:
        return self.stack_2[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()