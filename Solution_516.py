class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        dp = [[0] * length for _ in range(length)]
        for i in range(length - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, length):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][length - 1]