# https://leetcode.com/problems/3sum

"""
+ Using 3 pointers
    + First at the beginning
    + Second: next to the first
    + Third: at the end

+ With first idx, I am going to find in range from firstIdx + 1 till end
    + If there are 3 elements summing together equals 0 
        => add to result
        => move left and right pointer to new elements (ignoring
        repetitive elements)
    + If summing 3 elements together is smaller than 0
        => increase second pointer
    + Otherwise
        => decrease third pointer

+ After looping first idx
    => move to a new element, ignoring repetitive element

Space complexity: O(N * N): N is length of array
Time complexity: O(1): 
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        i = 0
        result = []

        nums.sort()

        while i < n - 2:
            low, high = i + 1, n - 1

            while low < high:
                total_sum = nums[i] + nums[low] + nums[high]
                if total_sum == 0:
                    result.append([nums[i], nums[low], nums[high]])

                    # move to next different element
                    while low < high - 1 and nums[low] == nums[low + 1]:
                        low += 1
                    low += 1

                    # move to next different element
                    while low + 1 < high and nums[high] == nums[high - 1]:
                        high -= 1
                    high -= 1

                elif total_sum < 0:
                    low += 1
                else:
                    high -= 1


            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        
        return result