# https://leetcode.com/problems/path-sum/

"""
+ From root
    + One is go to left
    + One is go to right

+ When I am going, I will get currentSum subtract current value

+ At the end if node is leaf (don't have left and right node)
    + To get whether curentSum after subtracting value of root equals to 0 or not

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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        if (root.left is None and root.right is None):
            return targetSum == root.val

        left = self.hasPathSum(root.left, targetSum - root.val)
        
        right = self.hasPathSum(root.right, targetSum - root.val)

        return left or right