class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l, r = max(nums), sum(nums)
        while l <= r:
            mid = (l+r)//2
            i=0
            k = 0
            for j in range(len(nums)+1):
                s = sum(nums[i:j])
                if s> mid:
                    k+=1
                    i = j-1
                    continue
            k+=1
            if k <= m:
                r = mid - 1
            elif k > m:
                l = mid + 1
        return l