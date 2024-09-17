# https://leetcode.com/problems/is-subsequence/

# To compare between 2 characters of first string and second string
# If they match together => increase pointer of string s
# Always increase pointer of string t

# At the end, if pointer of string s is at the end => return True
# Space complexity: O(1)
# Time complexity: O(B)

class Solution(object):
    def isSubsequence(self, s, t):
        A, B = len(s), len(t)

        if(A > B):
            return False

        i = 0
        j = 0

        while j < B:
            if(i == A):
                return True

            if(s[i] == t[j]):
                i += 1

            j += 1 

        return i == A

solution = Solution()

result = solution.isSubsequence("b", "abc")
print("Result:", result)  
        