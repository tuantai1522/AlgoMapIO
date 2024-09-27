# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

"""
+ Move ahead pointer n + 1 step
+ Move ahead pointer and behind pointer while ahead pointer is not None
+ Update next pointer of behind pointer

Space complexity: O(1): 
Time complexity: O(N): N is length of head
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        ahead = behind = dummyNode

        for _ in range(n + 1):
            ahead = ahead.next

        while ahead:
            behind = behind.next
            ahead = ahead.next

        behind.next = behind.next.next

        return dummyNode.next
