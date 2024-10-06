# https://leetcode.com/problems/binary-tree-level-order-traversal

"""
+ Using queue technique
+ To start from root at the first level
    + If that root has left child node or right child node => add it to queueu
    + At the end, when finishing iterating one level => add it to result list

Space complexity: O(M): M is a number of Nodes in root Tree 
Time complexity: O(M): M is a number of Nodes in root Tree
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if not root:
            return result

        queue = deque()

        queue.append(root)

        while len(queue) != 0:
            temp = []
            size = len(queue)
            while size != 0:
                node = queue.popleft()
                temp.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                size -= 1

            result.append(temp)

        return result