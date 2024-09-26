# https://leetcode.com/problems/reverse-linked-list/

"""
+ Have the previous pointer and current pointer
+ Reverse direction of current pointer by pointing to previous pointer
+ Move 2 pointers to next iteration

Space complexity: O(1): 
Time complexity: O(N): N is length of head
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev = None
        cur = head

        while cur is not None:
            next = cur.next

            cur.next = prev

            prev = cur
            cur = next


        return prev

        


