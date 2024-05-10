# 122 Best Time to Buy and Sell Stock 2

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 1
        profit = 0
        while i < len(prices):
            while i < len(prices) and prices[i - 1] > prices[i]:
                i += 1
            profit -= prices[i - 1]
            while i < len(prices) and prices[i - 1] <= prices[i]:
                i += 1
            profit += prices[i - 1]
        return profit

#faster than 66.52%, memory less than 73.94%
