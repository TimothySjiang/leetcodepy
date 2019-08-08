class Solution:
    # @param {int} n an integer
    # @return {int} how much money you need to have to guarantee a win
    def getMoneyAmount(self, n):
        # Write your code here
        dp = [[0 for _ in range(n + 1)] for __ in range(n + 1)]
        for len in range(2, n + 1):
            for start in range(1, n - len + 2):
                temp = float('inf')
                for k in range(start + (len - 1) // 2, start + len - 1):
                    left, right = dp[start][k - 1], dp[k + 1][start + len - 1]
                    temp = min(k + max(left, right), temp)
                    if left > right:
                        break
                dp[start][start + len - 1] = temp

        return dp[1][n]