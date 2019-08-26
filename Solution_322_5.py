class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        n = len(coins)
        dp = [[0] * (amount + 1) for i in range(n)]
        for j in range(0, amount + 1):
            if not j % coins[0]:
                dp[0][j] = j // coins[0]
            else:
                dp[0][j] = -1

        for i in range(1, n):
            for j in range(0, amount + 1):
                if j < coins[i]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    temp = float('inf')
                    for k in range(0, j // coins[i] + 1):
                        remaining = j - coins[i] * k
                        if dp[i - 1][remaining] != -1 and dp[i - 1][remaining] + k < temp:
                            temp = dp[i - 1][remaining] + k
                    dp[i][j] = temp if temp < float('inf') else -1

        return dp[n - 1][amount]