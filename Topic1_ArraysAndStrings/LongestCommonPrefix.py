# https://leetcode.com/problems/longest-common-prefix/
"""
+ Get the minimum length of every string
+ To start with first idx and compare every idx of list string
    + If it is different => return string from 0 to that idx

Space complexity: O(1)
Time complexity: O(N * min(len(strs)))
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 1: 
            return strs[0]

        min_length = float("inf")

        for str in strs:
            min_length = min(min_length, len(str))
            
        i = 0
        while i < min_length:
            for str in strs:
                if(strs[0][i] != str[i]):
                    return strs[0][:i]

            i += 1

        return strs[0][:i]
        

        

