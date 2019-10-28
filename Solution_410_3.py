class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l, r = max(nums), sum(nums) + 1
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        while l < r:
            mid = l + (r-l)//2
            i = k = 0
            for j in range(1,len(nums)+1):
                if i == 0:
                    s = nums[j-1]
                else:
                    s = nums[j-1] - nums[i-1]
                if s> mid:
                    k+=1
                    i = j-1
                    continue
            k+=1
            if k > m:
                l = mid + 1
            else:
                r = mid
        return l