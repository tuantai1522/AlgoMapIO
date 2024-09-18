# https://leetcode.com/problems/summary-ranges/

"""
+ To assign min and max value is first element
+ To loop from second element
    + if there is any elements not in the range => add to result
    + Otherwise, update max value
Space complexity: O(1)
Time complexity: O(N)
"""

class Solution(object):
    def summaryRanges(self, nums):
        result = []

        if(len(nums) == 0):
            return result

        min, max = nums[0], nums[0]

        for idx in range(1, len(nums)):
            if(nums[idx] != nums[idx - 1] + 1):
                result.append((str(min)) + ("->") + (str(max)) if min != max else (str(min)))

                min = nums[idx]
                max = nums[idx]
            else:
                max = nums[idx]
        
        result.append((str(min)) + ("->") + (str(max)) if min != max else (str(min)))

        return result

        

        