class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        queue = [(0, 0)]
        level = 0
        visited = set()
        visited.add((0, 0))
        while queue:
            for i in range(len(queue)):
                x, y = queue.pop(0)
                if x == len(grid) - 1 and y == len(grid[0]) - 1:
                    return level + 1
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        newx = x + dx
                        newy = y + dy
                        if (dx or dy) and 0 <= newx < len(grid) and 0 <= newy < len(grid[0]) and grid[newx][
                            newy] != 1 and (newx, newy) not in visited:
                            visited.add((newx, newy))
                            queue.append((newx, newy))
            level += 1

        return -1