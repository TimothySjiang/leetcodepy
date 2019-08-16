class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not maze: return False
        start = (start[0], start[1])
        destination = (destination[0], destination[1])
        queue = [start]
        visited = set(start)
        while queue:
            for i in range(len(queue)):
                x, y = queue.pop(0)
                positions = self.roll(maze, (x, y))
                for pos in positions:
                    if pos == destination:
                        return True
                    if pos not in visited:
                        visited.add(pos)
                        queue.append(pos)
        return False

    def roll(self, maze, start):
        m = len(maze)
        n = len(maze[0])
        x, y = start
        results = []
        dx = [0, 0, -1, +1]
        dy = [-1, +1, 0, 0]
        for i in range(4):
            newx = x
            newy = y
            while newx >= 0 and newx < m and newy >= 0 and newy < n and maze[newx][newy] == 0:
                newx += dx[i]
                newy += dy[i]
            newx -= dx[i]
            newy -= dy[i]
            results.append((newx, newy))

        return results