class Solution:
    def search(self, nums, target):
        if not nums: return -1
        if len(nums) == 1: return 0 if nums[0] == target else -1
        pivot = self.findPivot(nums)
        if target == nums[pivot]:
            return pivot
        if pivot == 0:
            return self.Bsearch(nums, target)
        if target < nums[0]:
            ans = self.Bsearch(nums[pivot:], target)
            return pivot + ans if ans != -1  else -1
        else:
            return self.Bsearch(nums[:pivot], target)

    def findPivot(self, nums):
        if nums[0] < nums[-1]:
            return 0
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1]:
                return mid + 1
            if nums[mid] > nums[l]:
                l = mid + 1
            else:
                r = mid

    def Bsearch(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        return -1