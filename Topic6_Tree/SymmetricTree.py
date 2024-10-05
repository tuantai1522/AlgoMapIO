# https://leetcode.com/problems/symmetric-tree

"""
+ I am going to define a function with 2 same root passed in parameters
    + One is go to left
    + One is go to right

+ I will have 2 falsy conditions
    + if 2 values are different
    + if one of node in root is None

+ I will have 1 true condtion
    + Both nodes are None

+ Return result from 2 path ways

Space complexity: O(H): H is height of Tree
Time complexity: O(N): N is a number of Node in Tree
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSame(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if not root1 and not root2:
                return True

            if not root1 or not root2:
                return False

            if root1.val != root2.val:
                return False

            left = isSame(root1.left, root2.right)
            right = isSame(root1.right, root2.left)

            return left and right

        return isSame(root, root)
