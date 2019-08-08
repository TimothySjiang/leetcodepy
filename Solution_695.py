class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        def isLand(i, j):
            if grid[i][j] == 0:
                return 0
            else:
                grid[i][j] = 0
            count = 0
            if i - 1 >= 0:    count += isLand(i - 1, j)
            if i + 1 <= n - 1:  count += isLand(i + 1, j)
            if j - 1 >= 0:    count += isLand(i, j - 1)
            if j + 1 <= m - 1:  count += isLand(i, j + 1)

            return 1 + count

        n = len(grid)
        m = len(grid[0])
        maxArea = 0
        for i in range(n):
            for j in range(m):
                maxArea = max(isLand(i, j), maxArea)

        return maxArea

