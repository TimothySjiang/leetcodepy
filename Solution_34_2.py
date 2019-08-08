class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        l,r = 0,len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m

        if l < len(nums) and nums[l] == target:
            lower = l
        else:
            return [-1, -1]

        r = len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] <= target:
                l = m + 1
            else:
                r = m

        return [lower, l - 1]
