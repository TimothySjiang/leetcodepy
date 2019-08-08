class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if not nums: return 0
        i,j = 0,1
        while i < len(nums) - 1:
            if nums[i] != nums[i + 1]:
                nums[j] = nums[i + 1]
                j += 1

            i += 1

        return j