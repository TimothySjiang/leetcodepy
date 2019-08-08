class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        total = 0
        ans = n + 1

        for i in range(n):
            total += nums[i]
            while (total >= s):
                ans = min(ans, i + 1 - l)
                total -= nums[l]
                l += 1

        if ans == n + 1:
            return 0
        else:
            return ans