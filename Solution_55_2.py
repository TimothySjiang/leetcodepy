class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1, -1, -1):
            length = nums[i]
            nums[i] = False
            if i + length >= len(nums) - 1:
                nums[i] = True
            else:
                for j in range(1, length + 1):
                    if nums[i + j]:
                        nums[i] = True
                        break

        return nums[0]