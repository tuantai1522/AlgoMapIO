# https://leetcode.com/problems/invert-binary-tree

from typing import Optional

"""
+ From root
    + We can go to left Node until I can't find any node
    + We can go to right Node until I can't find any node
    + Update left and right pointer of root Node

Space complexity: O(H): H is height of Tree
Time complexity: O(N): N is a number of Node in Tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root