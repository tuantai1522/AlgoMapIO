# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

"""
+ Using In Order technique because the list will go in increasing
+ At the time we hit kth time in tree => it's answer

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = [0]
        count = [k]
        def inOrder (root: Optional[TreeNode]):
            if not root:
                return

            inOrder(root.left)
            count[0] -= 1
            if count[0] == 0:
                ans[0] = root.val
                return

            inOrder(root.right)

        inOrder(root)

        return ans[0]