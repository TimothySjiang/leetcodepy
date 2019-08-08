class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if not n or n == 1:
            return 0
        hold = [0] * n
        cash = [0] * n

        hold[0] = -prices[0]
        hold[1] = max(-prices[0], -prices[1])
        cash[0] = 0
        cash[1] = max(0, hold[0] + prices[1])

        for i in range(2, n):
            hold[i] = max(hold[i - 1], cash[i - 2] - prices[i])
            cash[i] = max(cash[i - 1], hold[i - 1] + prices[i])

        return cash[-1]