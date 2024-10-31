# https://leetcode.com/problems/permutation-in-string

"""
+ To run dfs from source until it reachs destination

    + When looping neighbours, we need to check whether that node exists or not
        + If not run dfs on that node
        + Otherwise, ignore that 
Time complexity: O(N + E): N is vertex, E is edge
Space complexity: O(N + E): N is vertex, E is edge
"""

from collections import defaultdict
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = [0] * n

        dict = defaultdict(list)

        for edge in edges:
            dict[edge[0]].append(edge[1])
            dict[edge[1]].append(edge[0])

        def dfs(source: int) -> bool:
            print(source, dict[source])
            if source == destination:
                return True

            for num in dict[source]:
                if visited[num] == 0:
                    visited[num] = 1

                    if dfs(num):
                        return True

            return False

        return dfs(source)