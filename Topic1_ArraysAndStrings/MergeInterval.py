#https://leetcode.com/problems/merge-intervals/

"""
+ To sort 2d array based on first element of 1d array
+ To get the end array of merged array as standard
    + If merged is empty or there is not overlapping => add it to merged array
    + If there is overlappding => update the last value of merged result

Space complexity: O(N)
Time complexity: O(N * logN)
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key = lambda x: x[0])
        
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1] = [min(merged[-1][0], interval[0]), max(merged[-1][1], interval[1])]

        return merged