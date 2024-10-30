# https://leetcode.com/problems/permutation-in-string

"""
+ To build 2 array containing frequency of character in every string
+ To count the frequency of every character in string s1

+ Based on length in s1, I am going to loop that length of window in s2
    + If the frequency of character in s1 equals frequency of character in s2 with length n => return True
Time complexity: O(N): N is length of string s2
Space complexity: O(1):
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        counts_s1 = [0] * 26
        counts_s2 = [0] * 26

        for idx in range(n):
            counts_s1[ord(s1[idx]) - 97] += 1
            counts_s2[ord(s2[idx]) - 97] += 1

        if counts_s1 == counts_s2:
            return True

        for idx in range(n, m):
            if counts_s1 == counts_s2:
                return True

            counts_s2[ord(s2[idx]) - 97] += 1
            counts_s2[ord(s2[idx - n]) - 97] -= 1
            
        
        return True if counts_s1 == counts_s2 else False