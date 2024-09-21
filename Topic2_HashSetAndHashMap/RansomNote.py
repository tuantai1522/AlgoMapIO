# https://leetcode.com/problems/ransom-note/

"""
+ First step: 
    To build dictionary with key is current character and its value is a frequency of occurence in magazine 
+ Second step: 
    + To check ransomNote string
        + if current character doesn't exist in dictionary => return False
        + if a frequence of current character is 1 => delete that 
        + if a frequence of current character is different from 1 => minus 1 value based on key in dictionary
        
Space complexity: O(26): 26 is a length of alphabet
Time complexity: O(N + M): N is length of magazine, M is length of ransomNote
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}

        for str in magazine:
            if str in dict:
                dict[str] += 1
            else:
                dict[str] = 1

        for str in ransomNote:
            if str in dict:
                dict[str] -= 1
                if dict[str] == 0:
                    del dict[str]
            else:
                return False
        
        return True

