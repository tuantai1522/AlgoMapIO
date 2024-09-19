#https://leetcode.com/problems/product-of-array-except-self

"""
+ To initialize 2 arrays, left and right array
    + With left array, every element if a produt on its left side
    + With right array, every element if a produt on its right side

+ To multiple 2 arrays together
Space complexity: O(N)
Time complexity: O(N)
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_arr  = [1] * n
        right_arr  = [1] * n

        for idx in range(1, len(nums)):
            left_arr[idx] = nums[idx - 1] *  left_arr[idx - 1]

        for idx in range(len(nums) - 2, -1, -1):
            right_arr[idx] = nums[idx + 1] *  right_arr[idx + 1]

        return [l * r for l, r in zip(left_arr, right_arr)]
    

solution = Solution()
result = solution.productExceptSelf([1,2,3,4])
print(result)