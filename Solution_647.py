class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(i + 1):
                if(s[j] == s[i] and (i - j <= 2 or dp[j + 1][i - 1] == 1)):
                    dp[j][i] = 1
                    count += 1
        return count