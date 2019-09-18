#Merge Sort
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)-1):
            res = max(res,abs(nums[i]-nums[i+1]))
        return res