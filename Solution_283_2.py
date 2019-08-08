class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = []
        for i, x in enumerate(nums):
            if x == 0:
                pos.append(i)
            else:
                if pos:
                    index = pos.pop(0)
                    nums[i] = 0
                    pos.append(i)
                    nums[index] = x
