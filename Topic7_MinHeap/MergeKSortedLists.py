# https://leetcode.com/problems/merge-k-sorted-lists

"""
+ To build heap with first element in every single list
    + First: value
    + Second: idx (to identify difference between 2 same values)
    + Third: node

+ To loop until heap is None
    + Pop the first element and push the next element of current node into heap
    + Get that pop element and push it into array
    
Space complexity: O(K): K is length of 2d array
Time complexity: O(N * logk): N is total elements of 2d array
"""
import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))

        result = ListNode(-1)
        cur = result

        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return result.next