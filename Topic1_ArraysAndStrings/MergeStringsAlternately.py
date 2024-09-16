# https://leetcode.com/problems/merge-strings-alternately/description/

# To find smaller len between 2 strings
# Loop to build string based on smaller string
# + At the end, to check if len of first string is larger
#   => add another characters of first string to result
# + Otherwise, add another characters of second string to result

# Space complexity: O(A + B)
# Time complexity: O(max(A, B))

class Solution:
    def mergeAlternately(self, word1, word2):
        result = []
        A, B = len(word1), len(word2)

        length = min(A, B)
        for i in range(length):
            result.append(word1[i])
            result.append(word2[i])

        result.append(word1[length:] if A > B else word2[length:])

        return ''.join(result)

solution = Solution()

result = solution.mergeAlternately("abc", "pqr")
print("Result:", result)

result = solution.mergeAlternately("ab", "pqr")
print("Result:", result)

result = solution.mergeAlternately("abc", "pq")
print("Result:", result)
