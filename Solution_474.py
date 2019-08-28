class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (m + 1) for i in range(n + 1)]
        for s in strs:
            zeros = ones = 0
            for c in s:
                if c == '1':
                    ones += 1
                else:
                    zeros += 1

            for i in range(n, ones - 1, -1):
                for j in range(m, zeros - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - ones][j - zeros] + 1)

        return dp[-1][-1]