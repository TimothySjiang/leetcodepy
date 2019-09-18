class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = float('inf')
        for i in range(len(nums)):
            if abs(nums[i]) < len(nums):
                nums[abs(nums[i])] = -abs(nums[abs(nums[i])])
            elif abs(nums[i]) == len(nums):
                nums[0] = -abs(nums[0])

        for i in range(1, len(nums)):
            if nums[i] > 0: return i
        if nums[0] > 0: return len(nums)
        return len(nums) + 1
