# https://leetcode.com/problems/balanced-binary-tree

from typing import Optional

"""
+ From root
    + We can go to left Node and plus 1 (plus one depth) until I can't find any node
    + We can go to right Node and plus 1 (plus one depth) until I can't find any node

    + If the difference between depth of left and right node is larger than 1
        => return -1

    + Otherwise 
        => return maximum depth of root

Space complexity: O(H): H is height of Tree
Time complexity: O(N): N is a number of Node in Tree
"""

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return True

        left = self.countDepth(root.left)
        if left == -1:
            return -1

        right = self.countDepth(root.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return max(left, right) + 1;

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.countDepth(root) != -1