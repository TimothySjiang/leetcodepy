class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        ball = (ball[0], ball[1], 0, '')
        queue = [ball]
        visited = [[(float('inf'), '')] * len(maze[0]) for _ in range(len(maze))]
        visited[ball[0]][ball[1]] = (0, '')
        while queue:
            for i in range(len(queue)):
                x, y, d, dr = queue.pop(0)
                positions = self.roll(maze, (x, y, d, dr), hole)
                for pos in positions:
                    x, y, d, dr = pos
                    if (d, dr) < visited[x][y]:
                        visited[x][y] = (d, dr)
                        queue.append(pos)
        return visited[hole[0]][hole[1]][1] if visited[hole[0]][hole[1]][0] != float('inf') else 'impossible'

    def roll(self, maze, start, hole):
        m = len(maze)
        n = len(maze[0])
        x, y, d, dr = start
        results = []
        for i in range(x - 1, -1, -1):
            if [i, y] == hole:
                results.append((i, y, d + x - i, dr + 'u'))
                break
            if maze[i][y] == 1:
                results.append((i + 1, y, d + x - i - 1, dr + 'u'))
                break
            if i == 0 and maze[i][y] != 1: results.append((i, y, d + x - i, dr + 'u'))
        for i in range(x + 1, m):
            if [i, y] == hole:
                results.append((i, y, d + i - x, dr + 'd'))
                break
            if maze[i][y] == 1:
                results.append((i - 1, y, d + i - 1 - x, dr + 'd'))
                break
            if i == m - 1 and maze[i][y] != 1: results.append((i, y, d + i - x, dr + 'd'))
        for j in range(y - 1, -1, -1):
            if [x, j] == hole:
                results.append((x, j, d + y - j, dr + 'l'))
                break
            if maze[x][j] == 1:
                results.append((x, j + 1, d + y - j - 1, dr + 'l'))
                break
            if j == 0 and maze[x][j] != 1: results.append((x, j, d + y - j, dr + 'l'))
        for j in range(y + 1, n):
            if [x, j] == hole:
                results.append((x, j, d + j - y, dr + 'r'))
                break
            if maze[x][j] == 1:
                results.append((x, j - 1, d + j - 1 - y, dr + 'r'))
                break
            if j == n - 1 and maze[x][j] != 1: results.append((x, j, d + j - y, dr + 'r'))

        return results