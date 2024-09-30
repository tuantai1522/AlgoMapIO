# https://leetcode.com/problems/copy-list-with-random-pointer/

"""
+ To use dictionary
    + Key: old address of node
    + Val: new address of node

+ To build list based on that dictionary


Space complexity: O(N): N is length of list
Time complexity: O(N): N is length of list
"""

from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head

        dict = {}
        
        cur_r = head
        while cur_r:
            node = Node(cur_r.val)
            dict[cur_r] = node
            cur_r = cur_r.next
            
        cur_r = head
        while cur_r:
            newNode = dict[cur_r]
            newNode.next = dict[cur_r.next] if cur_r.next else None
            newNode.random = dict[cur_r.random] if cur_r.random else None
            cur_r = cur_r.next

        return dict[head]


        