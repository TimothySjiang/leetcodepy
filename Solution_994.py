#Freaking out testing!!!!
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        m = len(grid)
        n = len(grid[0])
        total = 0
        t = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    total += 1
                    if grid[i][j] == 2:
                        queue.append((i, j, t))

        while queue:
            total -= len(queue)
            for i in range(len(queue)):
                x, y, t = queue.pop(0)
                if x + 1 < m and grid[x + 1][y] == 1:
                    grid[x + 1][y] = 3
                    queue.append((x + 1, y, t + 1))
                if x - 1 >= 0 and grid[x - 1][y] == 1:
                    grid[x - 1][y] = 3
                    queue.append((x - 1, y, t + 1))
                if y + 1 < n and grid[x][y + 1] == 1:
                    grid[x][y + 1] = 3
                    queue.append((x, y + 1, t + 1))
                if y - 1 >= 0 and grid[x][y - 1] == 1:
                    grid[x][y - 1] = 3
                    queue.append((x, y - 1, t + 1))

        if not total: return t
        return -1
