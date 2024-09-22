#https://leetcode.com/problems/maximum-number-of-balloons

"""
+ First step: To build dictionary based on "balloon" string
+ Second step: To check every key in dictionary is in "balloon" string or not
    + If it's not => return False
    + Otherwise, get the minimum "balloon" string I can build

Space complexity: O(M): M is length of "balon" string
Time complexity: O(N): N is length of text string
"""

from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dict = defaultdict(int)
        balloon = "balloon"

        for s in text:
            if s in balloon:
                dict[s] += 1

        if any(c not in dict for c in balloon):
            return 0
        else:
            return min(dict['b'], dict['a'], dict['l'] // 2, dict['o'] // 2, dict['n']) 