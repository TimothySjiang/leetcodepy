class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return nums[0] == target

        pivot = self.findPivot(nums)

        return self.BinarySearch(nums[:pivot], target) or self.BinarySearch(nums[pivot:], target)

    def BinarySearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            else:
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return False

    def findPivot(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i + 1
        return 0
