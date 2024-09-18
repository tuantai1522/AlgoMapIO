#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

"""
Always get the minimum value in array => buy min sell max
Calculating current profit 

Space complexity: O(1)
Time complexity: O(N)
"""

class Solution(object):
    def maxProfit(self, prices):
        result = 0
        buy = prices[0]
        for price in prices:
            buy = min(buy, price)

            result = max(result, price - buy)

        return result