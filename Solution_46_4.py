class Solution:
    def permute(self, nums):
        if not nums: return [[]]
        results = []
        for i in range(len(nums)):
            newNums = nums[:]
            newNums.pop(i)
            results += ([[nums[i]]+ x for x in self.permute(newNums)])
        return results