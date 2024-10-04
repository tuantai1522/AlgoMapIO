# https://leetcode.com/problems/same-tree/
"""
+ From root of p and q
    + if total root is NULL => Same => return true
    + if one of the root is NULL but other is not NULL => Different => return false
    + if values of 2 nodes are different => Different => return False

+ Return boolean value between left and right node

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right
            