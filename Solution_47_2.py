#Great!
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            newnums = nums[:i] + nums[i + 1:]
            self.recursion(newnums, result + [nums[i]], results)

        return results

    def recursion(self, nums, result, results):
        if not nums:
            results.append(result)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            newnums = nums[:i] + nums[i + 1:]
            self.recursion(newnums, result + [nums[i]], results)