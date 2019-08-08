class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if not n:
            return [[]]

        result = []
        for i in range(len(nums) - 1):
            result += [[nums[i]] + x for x in self.permute(nums[:i] + nums[i + 1:])]

        result += [[nums[-1]] + x for x in self.permute(nums[:-1])]

        return result