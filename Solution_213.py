class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) <= 3: return max(nums)
        return max(self.helprob(nums[1:]), self.helprob(nums[:-1]))

    def helprob(self, nums):
        prevMax = nums[0]
        currMax = max(nums[0:2])
        for i in range(2, len(nums)):
            temp = max(prevMax + nums[i], currMax)
            prevMax = currMax
            currMax = temp
        return currMax