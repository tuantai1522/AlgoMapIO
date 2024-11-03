# https://leetcode.com/problems/course-schedule/

"""
+ To run dfs on every single course I have

+ There are 3 states of each course
    + UNVISITED: 0
    + VISITING: 1
    + VISITED: 2

+ If that course is already visited: -> True (learned that before)
+ If that course is currently on the path I try -> False (cycle)

+ Otherwise, run dfs on that course
    + To update that course as visited

Time complexity: O(N + E): N is a number of courses, E is a number of paths
Space complexity: O(N): N is a number of courses
"""

from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dict = defaultdict(list)

        for prerequisite in prerequisites:
            dict[prerequisite[0]].append(prerequisite[1])

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        def dfs(cur_course: int) -> bool:
            if visited[cur_course] == VISITED:
                return True

            if visited[cur_course] == VISITING:
                return False

            visited[cur_course] = VISITING

            for course in dict[cur_course]:
                if dfs(course) == False:
                    return False

            visited[cur_course] = VISITED
            
            return True
            
        visited = [UNVISITED] * numCourses
        for course in range(numCourses):
            if(dfs(course) == False):
                return False
        
        return True
        




