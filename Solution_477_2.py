class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        bitNumZero = [0] * 32
        bitNumOne = [0] * 32
        for i in range(32):
            for num in nums:
                if (num >> i) & 1:
                    bitNumOne[i] += 1
                else:
                    bitNumZero[i] += 1
        count = 0
        for i in range(32):
            count += bitNumZero[i] * bitNumOne[i]
        return count