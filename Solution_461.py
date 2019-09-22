class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        for i in range(32):
            count += ((x >> i) & 1) != ((y >> i) & 1)
        return count