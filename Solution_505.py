class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        start = (start[0], start[1],0)
        queue = [start]
        visited = [[float('inf')]*len(maze[0]) for _ in range(len(maze))]
        visited[start[0]][start[1]] = 0
        while queue:
            for i in range(len(queue)):
                x, y, d = queue.pop(0)
                positions = self.roll(maze, (x, y, d))
                for pos in positions:
                    x,y,d = pos
                    if d < visited[x][y]:
                        visited[x][y] = d
                        queue.append(pos)
        return visited[destination[0]][destination[1]] if visited[destination[0]][destination[1]] != float('inf') else -1

    def roll(self, maze, start):
        m = len(maze)
        n = len(maze[0])
        x, y, d = start
        results = []
        dx = [0, 0, -1, +1]
        dy = [-1, +1, 0, 0]
        for i in range(4):
            newx = x
            newy = y
            newd = d
            while newx >= 0 and newx < m and newy >= 0 and newy < n and maze[newx][newy] == 0:
                newx += dx[i]
                newy += dy[i]
                newd += 1
            newx -= dx[i]
            newy -= dy[i]
            newd -= 1
            results.append((newx, newy,newd))

        return results