# https://leetcode.com/problems/group-anagrams

"""
+ First step: To build array based on a frequency of every character in every string
+ Second step: To build tuple from that char array after finishing iterating one string
+ Third step: add it to dict
+ Return values of dict

Space complexity: O(N): N is length of list
Time complexity: O(N * M): N is length of list, M is length of every string
"""


from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        dict = defaultdict(list)
        
        if len(strs) == 0:
            return result

        for s in strs:
            char_arr = [0] * 26
            for c in s:
                char_arr[ord(c) - ord('a')] += 1

            key = tuple(char_arr) # to create key based on char_arr

            dict[key].append(s)

        return dict.values()