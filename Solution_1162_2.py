#TLE
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = [[float('inf')] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(i, j, grid, result)
        res = -1
        for i in range(m):
            for j in range(n):
                if result[i][j] < float('inf'):
                    res = max(res, result[i][j])
        return res

    def bfs(self, i, j, grid, result):
        queue = [(i, j)]
        level = 0
        visited = set()
        found = False
        while queue:
            for i in range(len(queue)):
                x, y = queue.pop(0)
                if grid[x][y] == 0:
                    result[x][y] = min(result[x][y], level)
                if x - 1 >= 0 and (x - 1, y) not in visited:
                    visited.add((x - 1, y))
                    queue.append((x - 1, y))
                if x + 1 < len(grid) and (x + 1, y) not in visited:
                    visited.add((x + 1, y))
                    queue.append((x + 1, y))
                if y - 1 >= 0 and (x, y - 1) not in visited:
                    visited.add((x, y - 1))
                    queue.append((x, y - 1))
                if y + 1 < len(grid[0]) and (x, y + 1) not in visited:
                    visited.add((x, y + 1))
                    queue.append((x, y + 1))
            level += 1