class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        res = float('-inf')
        dp = [collections.defaultdict(int) for i in range(len(A) + 1)]
        for i in range(len(A)):
            for j in range(i):
                arithmetic = A[i] - A[j]
                if arithmetic in dp[j + 1]:
                    dp[i + 1][arithmetic] = max(dp[i + 1][arithmetic], 1 + dp[j + 1][arithmetic])
                else:
                    dp[i + 1][arithmetic] = 2
                res = max(res, dp[i + 1][arithmetic])
        return res
