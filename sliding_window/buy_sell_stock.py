# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and 
# choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        lowestPrice = float('inf')
        
        for i in prices:
            
            if i < lowestPrice:
                lowestPrice = i
            
            maxProfit = max(maxProfit, i - lowestPrice)
            
        return maxProfit

# Test Cases
sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))
prices = [7,6,4,3,1]
print(sol.maxProfit(prices))