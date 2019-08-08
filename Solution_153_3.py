class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        pivot = self.findPivot(nums)
        return nums[pivot]

    def findPivot(self, nums):
        left = 0
        right = len(nums) - 1

        if nums[left] < nums[right]:
            return 0

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return mid + 1
            else:
                if nums[mid] > nums[left]:
                    left = mid + 1
                else:
                    right = mid