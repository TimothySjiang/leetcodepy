class Solution:
    def trailingZeroes(self, n: int) -> int:
        if not n: return 0
        return n//5 + self.trailingZeroes(n // 5)