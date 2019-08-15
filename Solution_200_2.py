class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
        return count

    def dfs(self, grid, i, j):
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)