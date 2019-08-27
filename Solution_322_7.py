class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        n = len(coins)
        dp = [float('inf')] * (amount + 1)
        for j in range(0, amount + 1):
            if not j % coins[0]:
                dp[j] = j // coins[0]

        for i in range(1, n):
            for j in range(coins[i], amount + 1):
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)

        return dp[-1] if dp[-1] < float('inf') else -1