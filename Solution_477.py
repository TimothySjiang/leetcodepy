#TLE
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                res += self.hammingDistance(nums[i], nums[j])
        return res

    def hammingDistance(self, num1, num2):
        new = num1 ^ num2
        count = 0
        maxL = max([num1.bit_length(), num2.bit_length()])
        for i in range(maxL):
            count += (new >> i) & 1
        return count