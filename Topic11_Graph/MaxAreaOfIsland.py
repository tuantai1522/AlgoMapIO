# https://leetcode.com/problems/max-area-of-island/

"""
+ To run dfs on every cell if that cell exists (equals 1)
    + Move on top
    + Move on left
    + Move on bottom
    + Move on right

+ If it reaches '0' cell (not island) or '2' cell (visited) -> return

+ To loop every single cell in grid
    + If that equals to 1 => count new area and compares with result

Time complexity: O(M * N * 4!): M is rows, N is columns
Space complexity: O(M * N ): M is rows, N is columns
"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i: int, j: int, area: List[int]):
            if i < 0 or i == m or j < 0 or j == n or grid[i][j] == 0 or grid[i][j] == 2:
                return

            grid[i][j] = 2
            area[0] += 1

            dfs(i + 1, j, area)
            dfs(i - 1, j, area)
            dfs(i, j + 1, area)
            dfs(i, j - 1, area) 

        area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total = [0]
                    dfs(i, j, total)
                    area = max(area, total[0])
        
        return area