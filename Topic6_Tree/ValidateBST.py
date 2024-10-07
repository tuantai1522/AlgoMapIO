# https://leetcode.com/problems/validate-binary-search-tree


"""
+ Using In Order technique because the list will go in increasing
+ I will use previvous pointer to store value of previous TreeNode of current Node
+ If there is somewhere it is not going increasing -> False

Space complexity: O(H): H is length of Tree 
Time complexity: O(N): N is a number of Node in tree
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    prev = None
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left = self.isValidBST(root.left)

        if self.prev is not None:
            if self.prev.val >= root.val:
                return False

        self.prev = root

        right = self.isValidBST(root.right)

        return left and right