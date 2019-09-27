class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        results = [[[0, 0] for i in range(n)] for i in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(i, j, grid, results)
                    count += 1

        res = float('inf')
        for i in range(m):
            for j in range(n):
                if not grid[i][j] and results[i][j][1] == count:
                    res = min(res, results[i][j][0])
        return res if res != float('inf') else -1

    def bfs(self, i, j, grid, results):
        queue = [(i, j)]
        dis = 0
        m = len(grid)
        n = len(grid[0])
        visited = set()
        visited.add((i, j))
        while queue:
            for i in range(len(queue)):
                x, y = queue.pop(0)
                if x - 1 >= 0 and grid[x - 1][y] not in (1, 2) and (x - 1, y) not in visited:
                    visited.add((x - 1, y))
                    queue.append((x - 1, y))
                if x + 1 < m and grid[x + 1][y] not in (1, 2) and (x + 1, y) not in visited:
                    visited.add((x + 1, y))
                    queue.append((x + 1, y))
                if y - 1 >= 0 and grid[x][y - 1] not in (1, 2) and (x, y - 1) not in visited:
                    visited.add((x, y - 1))
                    queue.append((x, y - 1))
                if y + 1 < n and grid[x][y + 1] not in (1, 2) and (x, y + 1) not in visited:
                    visited.add((x, y + 1))
                    queue.append((x, y + 1))
                results[x][y][0] += dis
                results[x][y][1] += 1
            dis += 1