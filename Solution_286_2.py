class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        m = len(rooms)
        n = len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    self.bfs(rooms, i, j)

    def bfs(self, rooms, i, j):
        m = len(rooms)
        n = len(rooms[0])
        stack = [(i, j)]
        level = 0
        while stack:
            for temp in range(len(stack)):
                px, py = stack.pop(0)
                rooms[px][py] = level

                if px - 1 > -1 and rooms[px - 1][py] > level:
                    stack.append((px - 1, py))
                if px + 1 < m and rooms[px + 1][py] > level:
                    stack.append((px + 1, py))
                if py - 1 > -1 and rooms[px][py - 1] > level:
                    stack.append((px, py - 1))
                if py + 1 < n and rooms[px][py + 1] > level:
                    stack.append((px, py + 1))

            level += 1
