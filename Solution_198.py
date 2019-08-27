class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        prevMax = nums[0]
        currMax = max(nums[0:2])
        for i in range(2,len(nums)):
            temp = max(prevMax+nums[i],currMax)
            prevMax = currMax
            currMax = temp
        return currMax