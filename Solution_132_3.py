class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        res = []
        dp = [[0 for x in range(n)] for x in range(n)]
        for i in range(n+1):
            res.append(i-1)
        res[0] = 0
        for i in range(n):
            for j in range(i+1):
                if (s[j] == s[i] and (i - j <= 2 or dp[j + 1][i-1])):
                    dp[j][i] = 1
                    if j == 0:
                        res[i+1] = 0
                    else:
                        res[i+1] = min(res[i+1], res[j] + 1)
        return res[n]