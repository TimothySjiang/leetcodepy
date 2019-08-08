class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        s = []
        res = (float('inf'),0)
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                res = min((abs(s-target),s),res)
                if s < target:
                    l +=1
                elif s > target:
                    r -= 1
                else:
                    return target
        return res[1]
