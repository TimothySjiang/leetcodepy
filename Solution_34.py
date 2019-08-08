class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1

        if nums[l] == target:
            lower = l
        else:
            return [-1, -1]

        r = len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > target:
                r = m
            else:
                l = m + 1

        return [lower, l - 1]

