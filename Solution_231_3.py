class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        if (n >> 31) & 1 : return False
        for i in range(31):
            count += ((n>>i) & 1 )
        return count == 1