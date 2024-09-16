# https://leetcode.com/problems/find-closest-number-to-zero/

# To find the smallest value in arr, ignoring whether it's 
# negative or positive
# + At the end, to check if closest is negative and there is postive
# value in arr => return larger element (positive value)
# + Otherwise => return that element

# Space complexity: O(1)
# Time complexity: O(N)

class Solution:
    def findClosestNumber(self, nums):
        closest = nums[0]
        for n in nums:
            if abs(closest) < abs(n):
                closest = n
        
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest

solution = Solution()

result = solution.findClosestNumber([-4,-2,1,4,8])
print("Result:", result)
