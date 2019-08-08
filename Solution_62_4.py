class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.seen = {}
        return self.dp(m - 1, n - 1)

    def dp(self, i, j):
        if i < 0 or j < 0:
            return 0
        if i == 0 or j == 0:
            return 1
        if (i, j) not in self.seen:
            self.seen[(i, j)] = self.dp(i - 1, j) + self.dp(i, j - 1)

        return self.seen[(i, j)]
