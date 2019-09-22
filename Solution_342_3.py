class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (-num) == num and num & 0xaaaaaaaa == 0