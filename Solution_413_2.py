class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        size = len(A)
        if size in (0, 1, 2):
            return 0

        t = [A[i] - A[i - 1] for i in range(1, len(A))]
        dp = [0 for i in range(size)]
        res = 0
        for i in range(2, size):
            if t[i - 2] == t[i - 1]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 0

            res += dp[i]
        return res