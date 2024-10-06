# https://leetcode.com/problems/subtree-of-another-tree

"""
+ From root
    + We can go to left Node until I can't find any node
    + We can go to right Node until I can't find any node
    + Update left and right pointer of root Node

Space complexity: O(M * N): M is a number of Nodes in root Tree and N is a number of Nodes in root SubRoot
Time complexity: O(M + N): M is a number of Nodes in root Tree and N is a number of Nodes in root SubRoot
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if not root1 and not root2:
                return True

            if not root1 or not root2:
                return False

            if root1.val != root2.val:
                return False
            
            left = isSame(root1.left, root2.left)
            right = isSame(root1.right, root2.right)

            return left and right

        if isSame(root, subRoot):
            return True

        if not root:
            return False;

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right