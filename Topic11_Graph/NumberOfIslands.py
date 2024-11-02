# https://leetcode.com/problems/number-of-islands

"""
+ To run dfs on every cell if that cell exists (equals 1)
    + Move on top
    + Move on left
    + Move on bottom
    + Move on right

+ If it reaches '0' cell (not island) or '2' cell (visited) -> return

+ To loop every single cell in grid
    + If that equals to 1 => new island

Time complexity: O(M * N * 4!): M is rows, N is columns
Space complexity: O(M * N ): M is rows, N is columns
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)        
        n = len(grid[0]) 

        def dfs(i: int, j: int):
            if i < 0 or i == m or j < 0 or j == n or grid[i][j] == '0' or grid[i][j] == '2':
                return

            grid[i][j] = '2'

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)    

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    result += 1
                    dfs(i, j)
        
        return result


