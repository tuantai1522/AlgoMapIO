#https://leetcode.com/problems/jewels-and-stones/

"""
+ First step: To build set based on jewels
+ Second step: To check every single character in stones whether it exists in set or not
Space complexity: O(N): N is length of jewels
Time complexity: O(M): M is length of stones
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        count = 0

        for c in stones:
            if c in s:
                count += 1

        return count