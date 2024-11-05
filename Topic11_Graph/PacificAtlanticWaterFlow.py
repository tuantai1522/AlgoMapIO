# https://leetcode.com/problems/pacific-atlantic-water-flow

"""
+ To run dfs from border of pacific and atlantic ocean
    + At each cell, if that cell can flow to its neightbor 
        => add to result

    + At the end, find the intersection of two array 
        => result
    
Time complexity: O(M * N): M is rows, N is columns
Space complexity: O(M * N): M is rows, N is columns
"""


from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        set_pacific = set()
        queue_pacific = deque()

        for i in range(1, m):
            set_pacific.add((i, 0))
            queue_pacific.append((i, 0))

        for j in range(n):
            set_pacific.add((0, j))
            queue_pacific.append((0, j))

        set_atlantic = set()
        queue_atlantic = deque()

        for i in range(m):
            set_atlantic.add((i, n - 1))
            queue_atlantic.append((i, n - 1))

        for j in range(0, n - 1):
            set_atlantic.add((m - 1, j))
            queue_atlantic.append((m - 1, j))

        def canFlow(set_t: set, queue_q = deque) -> List[int]:
            while len(queue_q) != 0:
                i, j = queue_q.popleft()
                set_t.add((i, j))

                for i_off, j_off in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    newI = i + i_off
                    newJ = j + j_off

                    if (0 <= newI < m and
                        0 <= newJ < n and
                        (newI, newJ) not in set_t and
                        heights[i][j] <= heights[newI][newJ]):

                        queue_q.append((newI, newJ))
                        set_t.add((newI, newJ))

            return set_t

        pacific = canFlow(set_pacific, queue_pacific)
        atlantic = canFlow(set_atlantic, queue_atlantic)
        

        return list(set(pacific).intersection(atlantic))