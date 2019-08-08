class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = Sum = 0
        h = {}
        h[0] = 1
        for i in range(len(nums)):
            Sum += nums[i]
            if ((Sum - k) in h.keys()):
                count += h[Sum - k]
            h[Sum] = h.get(Sum, 0) + 1

        return count