# https://leetcode.com/problems/merge-two-sorted-lists/

"""
+ Compare 2 pointers to determine which val is smaller
+ If current value of list1 is smaller, add it to result list and move pointer of list1 to the next
+ Otherwise, do the reverse thing

+ At the end, if there is any list iterated till the end => add remaining list to result list

Space complexity: O(1): 
Time complexity: O(Max(M, N)): M is length of list1, N is length of list2
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(-1)
        temp = result
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next

            temp = temp.next
        
        temp.next = list1 if list1 else list2

        return result.next