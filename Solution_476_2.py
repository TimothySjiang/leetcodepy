class Solution:
    def findComplement(self, num: int) -> int:
        for i in range(num.bit_length()):
            flip = 1 << i
            num ^= flip
        return num