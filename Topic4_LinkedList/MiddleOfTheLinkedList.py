# https://leetcode.com/problems/middle-of-the-linked-list/

"""
+ Using slow and fast pointer
    + Slow moves only 1 step
    + Fast moves 2 steps

+ At the end
    + if fast is None (there are odd elements) => return slow
    + Otherwise (there are even elements) => return slow.next
    
Space complexity: O(1): 
Time complexity: O(N): N is length of list
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head

        slow = head
        fast = head.next

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow if fast is None else slow.next