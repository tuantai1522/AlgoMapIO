# https://leetcode.com/problems/longest-repeating-character-replacement

"""
+ To build array containing 26 uppercase English letters which are valid window
+ I am going to have 2 pointers: left and right
    + Left at the beginning
    + Right for iteration

+ At idx right
    + Always count frequency of that element
+ If range [left, right] is not in valid window (by getting range and minus maximum value in array)
    + Increase left pointer and decrease frequency of left element
one value

Time complexity: O(N): N is length of array
Space complexity: O(26): 
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        n = len(s)
        max_len = 0

        counts = [0] * 26
        for right in range(0, n):
            counts[ord(s[right]) - 65] += 1

            while (right - left + 1) - max(counts) > k:
                counts[ord(s[left]) - 65] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
        
        return max_len