class Solution:
    def permute(self, nums):
        if not nums: return [[]]
        return self.permuteHelp([], nums)

    def permuteHelp(self, cur, nums):
        results = []
        if len(nums) == 0:
            results.append(cur)
            return results

        for i in range(len(nums)):
            newCur = cur[:]
            newCur.append(nums[i])
            newNum = nums[:]
            newNum.pop(i)
            results += self.permuteHelp(newCur, newNum)

        return results
