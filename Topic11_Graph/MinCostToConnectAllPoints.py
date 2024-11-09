# https://leetcode.com/problems/min-cost-to-connect-all-points/


"""
+ Using Prim to find minimum spanning tree
    + I can start with node at 0 position
        + If that node in visited array => ignore that to avoid from cycle path
        + Otherwise loop its neighbours and if neighbour is not in visited array
            => push in queue to iterate that

Time complexity: O(N ^ 2 * log(N)): N is length of points
Space complexity: O(N ^ 2): N is length of points
"""

import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def countDistance(point1: List[int], point2: List[int]) -> int:
            return abs(abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]))

        n = len(points)

        visited = set()

        # Weight, node
        min_heap = [(0, 0)]

        result = 0

        while len(visited) < n:
            (weight, node) = heapq.heappop(min_heap)

            if node in visited:
                continue

            visited.add(node)
            
            result += weight

            for j in range(n):
                if j not in visited:
                    xj, yj = points[j]

                    weight = countDistance(points[node], points[j])

                    heapq.heappush(min_heap, (weight, j))

        return result