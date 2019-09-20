class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mask = 0xFFFFFFFF
        MAX = 0x7FFFFFFF
        bitnum = [0] * 32
        n = len(nums)
        res = 0
        for i in range(32):
            for j in range(n):
                bitnum[i] += (nums[j] >> i) & 1
            res |= ((bitnum[i] % 3) << i)

        return res if res <= MAX else ~(res ^ mask)