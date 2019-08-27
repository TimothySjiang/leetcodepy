class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [float('inf')] * len(triangle[-1])
        dp[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            temp = dp[:]
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(temp[max(j - 1, 0):j + 1])
        return min(dp)
