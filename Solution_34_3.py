class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1,-1]
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] >=target:
                right = mid
            else:
                left = mid + 1
        if left >= len(nums) or nums[left] != target:return [-1,-1]
        newleft = left
        right = len(nums)
        while newleft < right:
            mid = newleft + (right-newleft)//2
            if nums[mid] > target:
                right = mid
            else:
                newleft = mid + 1
        return [left,newleft-1]