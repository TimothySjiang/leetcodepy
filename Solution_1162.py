#TLE
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        self.dis = -1
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    self.bfs(i, j, grid)
        return self.dis

    def bfs(self, i, j, grid):
        queue = [(i, j)]
        level = 0
        visited = set()
        found = False
        while queue and not found:
            for i in range(len(queue)):
                x, y = queue.pop(0)
                if grid[x][y] == 1:
                    self.dis = max(self.dis, level)
                    found = True
                    break
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