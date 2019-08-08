class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            newNums = nums[:]
            newNums.pop(i)
            result += [[nums[i]] + x for x in self.permuteUnique(newNums)]
        return result