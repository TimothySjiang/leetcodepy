class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for i in range(n)]
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                if s[i + l - 1] == s[i] and (l <= 2 or dp[i + 1][i + l - 2]):
                    dp[i][i + l - 1] = True
        res = [0] + [i for i in range(n)]

        for i in range(1, n + 1):
            if dp[0][i - 1]:
                res[i] = 0
                continue
            for j in range(1, i):
                if dp[j][i - 1]:
                    res[i] = min(res[i], res[j] + 1)

        return res[-1]
