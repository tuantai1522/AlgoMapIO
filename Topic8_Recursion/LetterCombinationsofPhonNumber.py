# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

"""
+ I am going to loop from the beginning of digits array until the end

+ At every idx, I am going to run recursion at next idx after adding
current character into string

+ After that I will remove the last element for the next iteration


Space complexity: O(N): N is length of array storing in call stack
Time complexity: O(N * 4 ^ N): N is stored in call stack and 
4 is maximum length of answer
"""

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []

        result = []
        phoneNumbers = [
            "-1",
            "-1",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]

        def helper(idx: int, temp: str):
            if len(temp) == n:
                result.append(temp)
                return

            for i in range(idx, n):
                for char in phoneNumbers[int(digits[i])]:
                    temp += char

                    helper(i + 1, temp)

                    temp = temp[:-1]

        helper(0, '')
        return result