class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = 0
        for num in nums:
            diff ^= num
        diff &= -diff
        rets = [0] * 2
        for num in nums:
            if num & diff == 0:
                rets[0] ^= num
            else:
                rets[1] ^= num
        return rets