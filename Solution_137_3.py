class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            sum = 0
            for j in range(len(nums)):
                if (nums[j] >> i) & 1:
                    sum += 1
                    sum %= 3
            if sum:
                ans |= sum << i
        return ans