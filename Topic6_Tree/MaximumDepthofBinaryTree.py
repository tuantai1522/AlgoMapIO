# https://leetcode.com/problems/maximum-depth-of-binary-tree

from typing import Optional

"""
+ From root
    + We can go to left Node and plus 1 (plus one depth) until I can't find any node
    + We can go to right Node and plus 1 (plus one depth) until I can't find any node
    + Get the maximum depth between left and right node

Space complexity: O(H): H is height of Tree
Time complexity: O(N): N is a number of Node in Tree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = 1 + self.maxDepth(root.left)
        right = 1 + self.maxDepth(root.right)

        return max(left, right)