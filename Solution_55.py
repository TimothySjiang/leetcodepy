class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = len(nums) - 1
        for i in range(pos, -1, -1):
            if nums[i] + i >= pos:
                pos = i

        return pos == 0