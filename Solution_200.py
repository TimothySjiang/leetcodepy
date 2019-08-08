class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        nr = len(grid)
        nc = len(grid[0])
        numIsland = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    numIsland += 1
                    self.dfs(grid, r, c)
        return numIsland

    def dfs(self, grid, r, c):
        nr = len(grid)
        nc = len(grid[0])

        if (r < 0 or c < 0 or r >= nr or c >= nc or grid[r][c] == "0"):
            return

        grid[r][c] = "0"
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)

        if (grid == None or not len(grid)):
            return 0



