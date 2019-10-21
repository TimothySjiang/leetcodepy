class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        h = []
        count = 0
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j]:
                    h.append((forest[i][j], i, j))
        heapq.heapify(h)
        pos = (0, 0)
        while h:
            target = heapq.heappop(h)[1:]
            dis = self.bfs(forest, pos, target)
            if dis != -1:
                count += dis
            else:
                return -1
            pos = target
        return count

    def bfs(self, forest, start, end):
        queue = [start]
        level = 0
        visited = set()
        while queue:
            for i in range(len(queue)):
                x, y = queue.pop(0)
                if (x, y) == end:
                    return level
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    newx = x + dx
                    newy = y + dy
                    if 0 <= newx < len(forest) and 0 <= newy < len(forest[0]) and forest[newx][newy] != 0 and (
                    newx, newy) not in visited:
                        visited.add((newx, newy))
                        queue.append((newx, newy))
            level += 1
        return -1