class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i+j ==0 :
                    continue
                if i>=1 and j>=1:
                    grid[i][j] += min(grid[i-1][j],grid[i][j-1])
                elif i >= 1:
                     grid[i][j] += grid[i-1][j]
                elif j >= 1:
                    grid[i][j] += grid[i][j-1]
        return grid[-1][-1]