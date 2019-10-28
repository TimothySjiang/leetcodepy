#TLE WTF this still TLE??
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        dp = [[float('inf')]*(m+1) for i in range(n+1)]
        sub = [0] * (n+1)
        for i in range(n):
            sub[i+1] = sub[i] + nums[i]
        dp[0][0] = 0
        for i in range(1,n+1):
            for j in range(1,m+1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j],max(dp[k][j-1],sub[i]-sub[k]))
        return dp[n][m]