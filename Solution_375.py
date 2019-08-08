#unknown
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for l in range(2, n + 1):
            for start in range(1, n - l + 2):
                minres = float('inf')
                for piv in range(start, start + l - 1):
                    res = piv + max(dp[start][piv - 1], dp[piv + 1][start + l - 1])
                    minres = min(res, minres)
                dp[start][start + l - 1] = minres

        return dp[1][n]



