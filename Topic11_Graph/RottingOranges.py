# https://leetcode.com/problems/rotting-oranges/

"""
+ To loop every sigle cell to get rotten orange and count how many
oranges I have

+ When I iterate queue, it will count 1 minute
    + Add fresh orange of its neighbour into queue
    + Rotten all neighbours if possible 
    
Time complexity: O(M * N): M is rows, N is columns
Space complexity: O(M * N): M is rows, N is columns
"""

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        num_fresh = 0
        
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    num_fresh += 1

        if num_fresh == 0:
            return 0

        result = -1
        while queue:
            k = len(queue)
            result += 1
            for _ in range(k):
                i, j = queue.popleft()
                for i_off, j_off in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    newI = i + i_off
                    newJ = j + j_off

                    if (0 <= newI < m and
                        0 <= newJ < n and
                        grid[newI][newJ] == 1):
                        queue.append((newI, newJ))
                        num_fresh -= 1
                        grid[newI][newJ] = 2

        return result if num_fresh == 0 else -1