#TLE
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums: return
        start = float('inf')
        end = float('-inf')
        for i in range(1,len(nums)):
            while i and nums[i] < nums[i-1]:
                nums[i-1],nums[i] = nums[i],nums[i-1]
                start = min(start,i-1)
                end = max(end,i)
                i -= 1
        return end - start + 1 if start != float('inf') else 0