class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (1 + n)
        for j in range(2, 1 + n):
            for i in range(1, j):
                dp[j] = max(dp[j], max(i, dp[i])*max(j - i, dp[j - i]))
        return dp[n]