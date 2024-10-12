# https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
+ To write function to count distance of one point

+ To use minimum heap
    
+ At every element 
    + If len of heap is smaller than k => push it into heap
    + If len of heap is larger than K => pop and push after that

+ Return the kth maximum element at idx 0

Time complexity: O(n log k): n is length of List, k is length of heap
Space complexity: O(k): k is kth which solution defines
"""

import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:     

        heap = []   
        for num in nums:
            if len(heap) == k:
                heapq.heappushpop(heap, num)
            else:
                heapq.heappush(heap, num)

        return heap[0]