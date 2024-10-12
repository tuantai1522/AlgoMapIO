# https://leetcode.com/problems/k-closest-points-to-origin

"""
+ To write function to count distance of one point

+ To use maximum heap
+ Every element in heap is tuple
    + Key: a distance to origin
    + Valut: its point
    
+ At every point, after calculating the distance 
    + If len of heap is smaller than k => push it into heap
    + If len of heap is larger than K => pop and push after that

Space complexity: O(K)
Time complexity: O(N * logk): N length of array
"""

import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def countDistance(point: List[int]) -> float:
            return pow(point[0], 2) + pow(point[1], 2)

        heap = []
        for point in points:
            count = -countDistance(point)
            if len(heap) == k:
                heapq.heappushpop(heap, (count, point))
            else:
                heapq.heappush(heap, (count, point))

        return [value for (key, value) in heap]