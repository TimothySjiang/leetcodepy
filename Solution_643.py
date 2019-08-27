class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        dp = [0] * (len(nums) - k + 1)
        dp[0] = sum(nums[0:k])
        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] + nums[k + i - 1] - nums[i - 1]
        return max(dp) / k
