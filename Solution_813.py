class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        dp = [[0.0 for i in range(n + 1)] for j in range(K + 1)]
        sums = [0.0 for i in range(n + 1)]
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + A[i - 1]
            dp[1][i] = sums[i] / i
        for i in range(2, K + 1):
            for j in range(i, n + 1):
                for k in range(i - 1, j):
                    dp[i][j] = max(dp[i][j], dp[i - 1][k] + (sums[j]-sums[k]) / (j-k))
        return dp[K][n]