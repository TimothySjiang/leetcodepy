class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        prevmax = nums[0]
        currmax = max(nums[0], nums[1])

        for v in nums[2:-1]:
            temp = currmax
            currmax = max(currmax, prevmax + v)
            prevmax = temp

        currmax1 = currmax

        prevmax = nums[1]
        currmax = max(nums[1], nums[2])

        for v in nums[3:]:
            temp = currmax
            currmax = max(currmax, prevmax + v)
            prevmax = temp

        return max(currmax1, currmax)