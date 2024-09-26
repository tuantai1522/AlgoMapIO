# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""
+ If 2 nexted elements is the same => move the previous pointer to the next pointer of current pointer
+ Otherwise, move prev pointer to the next

+ Always move cur pointer to next for next iteration

Space complexity: O(1): 
Time complexity: O(N): N is length of head
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev = head
        cur = head.next

        while cur is not None:
            next = cur.next
            if cur.val == prev.val:
                prev.next = next
            else:
                prev = cur
            
            cur = next

        return head
