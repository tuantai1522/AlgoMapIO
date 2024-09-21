# https://leetcode.com/problems/valid-anagram/

"""
+ First step: 
    + Based on array containg 26 lowercase characters, count a frequency of first string by adding 1 value
+ Second step: 
    + Based on array containg 26 lowercase characters, count a frequency of second string by minusing 1 value
+ Second step: 
    + To check whether every element in array equals 0 or not
        
Space complexity: O(26): 26 is a length of alphabet
Time complexity: O(N + M + 26): M is length of s, T is length of t
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        M = len(s)
        T = len(t)

        if M != T: return False
        set = [0] * (26)

        for str in s:
            set[ord(str) - ord('a')] += 1

        for str in t:
            set[ord(str) - ord('a')] -= 1

        for num in set:
            if num != 0:
                return False

        return True
        