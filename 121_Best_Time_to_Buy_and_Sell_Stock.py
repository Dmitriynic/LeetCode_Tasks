# 121 Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = inf
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            if price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit'

#faster than 87.13%, memory less than 33.93%
