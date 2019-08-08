class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if (len(nums) == 1):
            return nums[0]

        prevMax = nums[0]
        currMax = max(nums[0], nums[1])

        for x in nums[2:]:
            temp = currMax
            currMax = max(currMax, prevMax + x)
            prevMax = temp

        return currMax