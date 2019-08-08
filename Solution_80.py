class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        i,j = 0,0
        nums += ['#','#']
        for i in range(len(nums)-2):
            if nums[i] != nums[i+2] :
                nums[j] = nums[i]
                j+=1
        return j