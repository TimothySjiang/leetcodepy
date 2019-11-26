class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if left >= len(nums) or nums[left] != target:
            return False
        first, right = left, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left - first > len(nums) // 2
