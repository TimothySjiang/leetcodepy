class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        self.res = []
        self.helpsubset(nums, 0, [])
        return self.res

    def helpsubset(self, nums, start, subset):
        self.res.append(subset)
        for i in range(start, len(nums)):
            self.helpsubset(nums, i + 1, subset + [nums[i]])
