# https://leetcode.com/problems/network-delay-time/

"""
+ To build adjacent list first

+ Min heap [x, y]
    + x is distance
    + y is Node
+ When iterating heap
    + Get heap and add all its neighbours into heap with minimum distance at the top

+ So when I get the first node in heap 
    => make sure to get the minimum value
    => if that node at top is visited -> ignore that

Time complexity: O(E log N): N is node, E is edge
Space complexity: O(N + E): N is node, E is edge
"""

from collections import defaultdict
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, time in times:
            adj[u].append((v, time))

        min_heap = [(0, k)]
        min_times = {}

        while min_heap:
            (weight, node) = heapq.heappop(min_heap)
            if node in min_times:
                continue

            min_times[node] = weight

            for nei, nei_time in adj[node]:
                if nei not in min_times:
                    heapq.heappush(min_heap, (weight + nei_time, nei))

        return max(min_times.values()) if len(min_times) == n else -1