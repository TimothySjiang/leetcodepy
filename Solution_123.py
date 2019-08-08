class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        minPrice = float('inf')
        maxProfit = 0
        profits = []
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
            profits.append(maxProfit)

        maxPrice = float('-inf')
        maxProfit = 0
        total = 0

        for i in range(len(prices) - 1, 0, -1):
            maxPrice = max(maxPrice, prices[i])
            maxProfit = max(maxProfit, maxPrice - prices[i])
            total = max(total, profits[i] + maxProfit)

        return total
