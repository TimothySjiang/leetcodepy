#better
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        new = x ^ y
        for i in range(32):
            count += (new >> i) & 1
        return count