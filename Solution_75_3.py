class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, index, right = 0, 0, len(nums) - 1
        while index <= right:
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
                index += 1
            elif nums[index] == 1:
                index += 1
            else:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1
