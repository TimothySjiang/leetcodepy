class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        return self.helpMin(grid, m - 1, n - 1)

    def helpMin(self, grid, i, j):
        if not grid or i < 0 or j < 0:
            return float('inf')
        if i == 0 and j == 0:
            return grid[0][0]
        return grid[i][j] + min(self.helpMin(grid, i - 1, j), self.helpMin(grid, i, j - 1))