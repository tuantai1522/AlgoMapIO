# https://leetcode.com/problems/minimum-absolute-difference-in-bst

"""
+ Using In Order technique because the list will go in increasing
+ At the middle, we will compare current value with the previous value
    + And get the minumum difference between 2 nodes

Space complexity: O(H): H is length of Tree 
Time complexity: O(M): M is a number of Nodes in root Tree
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    ans = float("inf")
    prev = None

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inOrder(root: Optional[TreeNode]):
            if not root:
                return

            inOrder(root.left)

            if self.prev is not None:
                self.ans = min(self.ans, abs(root.val - self.prev))

            self.prev = root.val

            inOrder(root.right)

        inOrder(root)

        return self.ans
    