class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 9

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] * (11 - i)

        return sum(dp)