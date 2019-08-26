class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if not amount: return 1
        if not coins: return 0

        dp = [[0] * (amount + 1) for i in range(len(coins))]
        for j in range(1, amount + 1):
            if not j % coins[0]:
                dp[0][j] = 1

        for i in range(1, len(coins)):
            for j in range(amount + 1):
                if j < coins[i]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    for k in range(0, j // coins[i] + 1):
                        if j == k * coins[i]:
                            dp[i][j] += 1
                        else:
                            dp[i][j] += dp[i - 1][j - k * coins[i]]

        return dp[-1][-1]
