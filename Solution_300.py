class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # write your code here
        if not nums:
            return 0
        dp = [1] * len(nums)
        for curr, val in enumerate(nums):
            for prev in range(curr):
                if nums[prev] < val:
                    dp[curr] = max(dp[curr], dp[prev] + 1)
        return max(dp)