# https://leetcode.com/problems/longest-substring-without-repeating-characters

"""
+ To build set to store unique elements of string
+ I am going to have 2 pointers: left and right
    + Left at the beginning
    + Right for iteration

+ At idx right, if that element at that idx is not in set
    + Add to set
+ Otherwise
    + Move left pointer to valid sliding window (without repeating characters)

Time complexity: O(N): N is length of array
Space complexity: O(N): N is length of array
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_t = set()
        longest = 0
        
        n = len(s)
        left = 0
        for right in range(n):
            if s[right] not in set_t:
                set_t.add(s[right])
            else:
                while s[right] in set_t:
                    set_t.remove(s[left])
                    left += 1

                set_t.add(s[right])
            
            longest = max(longest, right - left + 1)

        return longest