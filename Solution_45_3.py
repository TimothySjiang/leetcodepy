class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[0] = 0
        start = 0
        for i in range(1,len(nums)):
            for j in range(start,i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i],dp[j]+1)
                    break
                start = max(start,j)
        return  dp[-1]