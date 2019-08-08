class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def walk(i, j, length):
            if i < 0 or i > m - 1 or j < 0 or j > n - 1 or grid[i][j] == 3 or grid[i][j] == -1:
                return None
            else:
                if grid[i][j] == 2:
                    if length == m * n - obstacle:
                        nonlocal count
                        count += 1
                else:
                    grid[i][j] = 3
                    walk(i + 1, j, length + 1)
                    grid[i][j] = 0

                    grid[i][j] = 3
                    walk(i - 1, j, length + 1)
                    grid[i][j] = 0

                    grid[i][j] = 3
                    walk(i, j + 1, length + 1)
                    grid[i][j] = 0

                    grid[i][j] = 3
                    walk(i, j - 1, length + 1)
                    grid[i][j] = 0

        obstacle = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = [i, j]
                if grid[i][j] == -1:
                    obstacle += 1

        count = 0
        walk(start[0], start[1], 1)

        return count