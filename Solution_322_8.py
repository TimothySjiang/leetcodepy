#Tle
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        n = len(coins)
        dp = [[float('inf')] * (amount + 1) for i in range(n)]
        for j in range(0, amount + 1):
            if not j % coins[0]:
                dp[0][j] = j // coins[0]

        for i in range(1, n):
            for j in range(0, amount + 1):
                if j < coins[i]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    for k in range(0, j // coins[i] + 1):
                        remaining = j - coins[i] * k
                        dp[i][j] = min(dp[i][j],dp[i - 1][remaining] + k)

        return dp[- 1][-1] if dp[-1][-1] < float('inf') else -1