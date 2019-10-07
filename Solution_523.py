class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        Sum = 0
        h = {}
        h[0] = -1
        for i,num in enumerate(nums):
            Sum += num
            if k:
                Sum = Sum % k
            if Sum in h:
                if h[Sum] != i-1:
                    return True
            else:
                h[Sum] = i
        return False