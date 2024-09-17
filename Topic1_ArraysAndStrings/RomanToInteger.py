# https://leetcode.com/problems/roman-to-integer

# Add first character based on dictionary into result
# When looping string, always add value of current character based on dictionary
#   If value of current character is larer than value of previous character => minus 2 times
#   based on value of previous character

# Space complexity: O(1)
# Time complexity: O(N)

class Solution(object):
    def romanToInt(self, s):
        my_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = my_dict[s[0]]

        for idx in range(1, len(s)):
            result += my_dict[s[idx]]

            if(my_dict[s[idx - 1]] < my_dict[s[idx]]):
                result -= my_dict[s[idx - 1]] * 2

        return result
    
solution = Solution()

result = solution.romanToInt("MCMXCIV")
print("Result:", result)