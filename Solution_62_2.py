class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = [[0]*n for j in range(m)]
        count[0][0] = 1
        for i in range(m):
            for j in range(n):
                count[i][j] += self.helpCount(count, i - 1, j) + self.helpCount(count, i, j - 1)

        return count[-1][-1]

    def helpCount(self, count, i, j):
        if not count or i < 0 or j < 0:
            return 0
        else:
            return count[i][j]