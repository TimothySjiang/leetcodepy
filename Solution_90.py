class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.subsets = []
        self.helpsubset(nums, 0, [])
        return self.subsets

    def helpsubset(self, nums, start, subset):
        self.subsets.append(subset)
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            self.helpsubset(nums, i + 1, subset + [nums[i]])