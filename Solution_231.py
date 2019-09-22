class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if not n : return False
        while not n % 2:
            n //= 2
        return n == 1