#Tle
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        m = len(nums)-k + 1
        n = len(nums)-k + 1
        dp = [[0]*n for i in range(m)]
        dp[0][0] = sum(nums[0:k])/k
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + (nums[k+j-1] - nums[j-1])/k
        for i in range(1,m):
            for j in range(n-i):
                if not j:
                    dp[i][j] = (dp[i-1][j]*(k+i-1) + nums[k+i-1])/(k+i)
                else:
                    dp[i][j] = dp[i][j-1] + (nums[k+i+j-1] - nums[j-1])/(k+i)

        return max([max(x) for x in dp])