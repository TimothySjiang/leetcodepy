class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]

        return result