# https://leetcode.com/problems/linked-list-cycle

"""
+ Using slow and fast pointer
    + Slow moves only 1 step
    + Fast moves 2 steps

Space complexity: O(1): 
Time complexity: O(N): N is length of list
"""

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow = head
        fast = head.next

        while slow and fast and fast.next:
            if slow is fast:
                return True

            slow = slow.next
            fast = fast.next.next
        
        return slow == fast