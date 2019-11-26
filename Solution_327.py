#TLE
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        count = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i != 0:
                    if lower <= nums[j] - nums[i-1] <= upper:
                        count += 1
                elif lower <= nums[j] <= upper:
                    count += 1
        return count