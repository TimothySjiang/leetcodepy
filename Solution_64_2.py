class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        i = 0
        j = 0
        for i in range(n):
            for j in range(m):
                if not i and not j:
                    continue
                grid[i][j] += min(self.helpMin(grid, i - 1, j), self.helpMin(grid, i, j - 1))

        return grid[n - 1][m - 1]

    def helpMin(self, grid, i, j):
        n = len(grid)
        m = len(grid[0])
        if not grid or not 0 <= i <= n - 1 or not 0 <= j <= m - 1:
            return float("inf")
        else:
            return grid[i][j]