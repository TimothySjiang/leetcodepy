class Solution:
    def permute(self, nums):
        if not nums: return [[]]
        results = []
        self.permuteHelp(results, nums, 0)
        return results

    def permuteHelp(self, results, nums, index):
        if index == len(nums):
            results.append(nums[:])
            return
        else:
            for i in range(index, len(nums)):
                self.swap(nums, index, i)
                self.permuteHelp(results, nums, index + 1)
                self.swap(nums, index, i)

    def swap(self, nums, i, j):
        temp = nums[j]
        nums[j] = nums[i]
        nums[i] = temp