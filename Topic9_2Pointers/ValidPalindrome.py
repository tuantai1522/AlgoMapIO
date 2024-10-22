# https://leetcode.com/problems/valid-palindrome

"""
+ Using 2 pointers
    + First at the beginning
    + Second at the end

+ To iterate until finding the first element in string which is 
non-alphanumeric characters
+ To iterate until finding the last element in string which is 
non-alphanumeric characters

+ Compare to each other by converting into lower character

+ If it's different => return False

+ Looping until left exceeds right pointer
+ Return True

Space complexity: O(N): N is length of string
Time complexity: O(1): 
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)

        left = 0
        right = n - 1

        while left < right:
            while left < n and not s[left].isalnum():
                left += 1

            while right >= 0 and not s[right].isalnum():
                right -= 1

            if left < right and s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True