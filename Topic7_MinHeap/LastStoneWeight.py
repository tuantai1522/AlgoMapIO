# https://leetcode.com/problems/last-stone-weight

"""
+ Using maximum heap => build max heap first
    + When I pop element in heap => get the largest element
    + When I pop next element in heap => get the next largest element

+ If these 2 values equal => do nothing
+ If it's different => push the difference again into heap
Space complexity: O(1)
Time complexity: O(N log N): N length of array
"""

import heapq
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)

        for i in range(n):
            stones[i] = - stones[i]
        
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, x - y)
            
        return stones[0] * -1 if len(stones) > 0 else 0

