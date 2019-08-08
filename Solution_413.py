class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        dp = [[0] * n for _ in range(n)]

        count = 0
        for i in range(n):
            for j in range(i + 2, n):
                if ((dp[i][j - 1]) or j - i == 2) and (A[j] - A[j - 1]) == (A[j - 1] - A[j - 2]):
                    dp[i][j] = 1
                    count += 1

        return count