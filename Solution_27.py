class Solution:
    def removeElement(self, nums: 'List[int]',val:int) -> 'int':
        if not nums:return 0
        i,j = 0,0
        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j