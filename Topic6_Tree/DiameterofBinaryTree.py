# https://leetcode.com/problems/diameter-of-binary-tree

from typing import Optional

"""
+ Using Helper function by storing maximum value
    + Froom root
        + To return the maximum path between left and right child node
        + To store maximum value of path of child nodes at every node

Space complexity: O(H): H is height of Tree
Time complexity: O(N): N is a number of Node in Tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    maxi = 0

    def getMaximumDiameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.getMaximumDiameterOfBinaryTree(root.left)
        right = self.getMaximumDiameterOfBinaryTree(root.right)

        self.maxi = max(self.maxi, left + right)

        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.getMaximumDiameterOfBinaryTree(root)

        return self.maxi