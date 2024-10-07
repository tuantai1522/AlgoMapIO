# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

"""
+ We always assume that root is always lowest common ancestor
    + if these 2 values are lower than root -> go to left
    + if these 2 values are higher than root -> go to right
    + if one of 2 values equals value of root -> return that node
    + if root is in between values of first and second node -> return that node

Space complexity: O(H): H is length of Tree 
Time complexity: O(H): H is length of Tree
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = [root]
        def search(root: 'TreeNode'):
            if not root:
                return

            lca[0] = root

            if root.val == p.val or root.val == q.val:
                return
            if p.val < root.val and q.val < root.val:
                search(root.left)
            elif p.val > root.val and q.val > root.val:
                search(root.right)
            else:
                return


        search(root)
        return lca[0]
