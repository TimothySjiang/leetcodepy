class Solution_121:
    def maxProfit(self,price):
        maxProfit , minPrice = 0 , int("inf")
        for price in prices:
            minPrice = min(minPrice,price)
            profit = price - minPrice
            maxProfit = max(profit,maxProfit)
        return maxProfit