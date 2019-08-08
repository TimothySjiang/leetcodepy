class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.helpCount(m - 1, n - 1)

    def helpCount(self, m, n):
        if m < 0 or n < 0:
            return 0
        if m == 0 and n == 0:
            return 1
        return self.helpCount(m - 1, n) + self.helpCount(m, n - 1)