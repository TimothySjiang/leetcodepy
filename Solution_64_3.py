class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def helpMin(i, j):
            if not grid or not 0 <= i <= n - 1 or not 0 <= j <= m - 1:
                return float("inf")
            else:
                return grid[i][j]

        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if not i and not j:
                    continue
                grid[i][j] += min(helpMin(i - 1, j), helpMin(i, j - 1))

        return grid[n - 1][m - 1]
