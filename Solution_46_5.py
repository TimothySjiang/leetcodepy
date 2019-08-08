class Solution:
    def permute(self, nums):
        return self.permuteHelp([], nums)

    def permuteHelp(self, cur, nums):
        results = []
        if len(cur) == len(nums):
            results.append(cur[:])
            return results
        for i in range(len(nums)):
            if nums[i] in cur:
                continue
            cur.append(nums[i])
            results += self.permuteHelp(cur, nums)
            cur.pop()
        return results