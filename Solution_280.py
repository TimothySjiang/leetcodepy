class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return

        for i in range(1, len(nums)):
            if i % 2:
                should_swap = nums[i] < nums[i - 1]
            else:
                should_swap = nums[i] > nums[i - 1]

            if should_swap:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]