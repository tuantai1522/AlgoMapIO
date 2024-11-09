# https://leetcode.com/problems/min-cost-to-connect-all-points/


"""
+ From original graph => to store in dictionary
    + Key: current Node
    + Value: new Node (for cloning)

+ When looping dictionary 
    -> I can build new graph based on key of dictionary

Time complexity: O(V + E): V is vertex, E is edge
Space complexity: O(E): E is edge
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        if len(node.neighbors)== 0:
            return Node(node.val)
        
        start = node
        dict = {}
        visited = set()
        def dfs(cur_node: Optional['Node']):
            if not cur_node:
                return

            if cur_node in visited:
                return

            visited.add(cur_node)

            for node in cur_node.neighbors:
                dict[cur_node] = Node(cur_node.val)
                dfs(node)

        dfs(node)

        for old_node, new_node in dict.items():
            for nei in old_node.neighbors:
                new_nei = dict[nei]
                new_node.neighbors.append(new_nei)

        return dict[start]


# 1 -> 2,4
# 2 -> 1,3
# 3 -> 2,4
# 4 -> 1,3