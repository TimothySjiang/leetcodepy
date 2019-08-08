class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        maxprofit = self.helpprofit(prices)
        for i in range(2, len(prices) - 1):
            maxprofit = max(maxprofit, self.maxProfit(prices[:i]) + self.maxProfit(prices[i:]))

        return maxprofit

    def helpprofit(self, p):
        buy_price = float('inf')
        profit = 0
        for i in range(len(p)):
            profit = max(p[i] - buy_price, profit)
            buy_price = min(buy_price, p[i])

        return profit
