class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        subsets = []
        self.helpsubset(nums, 0, [], subsets)
        return subsets

    def helpsubset(self, nums, start, subset, subsets):
        subsets.append(subset)
        for i in range(start, len(nums)):
            self.helpsubset(nums, i + 1, subset + [nums[i]], subsets)

