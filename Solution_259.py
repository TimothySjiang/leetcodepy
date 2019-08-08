class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        nums.sort()
        count = 0
        for i in range(len(nums)-2):
            l,r = i+1,len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < target:
                    count+= r-l
                    l += 1
                else:
                    r -= 1
        return count