class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1
        for i in range(1,len(nums)+1):
            if i not in nums:
                return i
        return i+1