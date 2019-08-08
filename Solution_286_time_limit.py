class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        n = len(rooms)
        m = len(rooms[0])

        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 2147483647:
                    rooms[i][j] = self.bfs(rooms, i, j)

    def bfs(self, rooms, i, j):
        n = len(rooms)
        m = len(rooms[0])
        stack = [(i, j)]
        level = 0
        while stack:
            for temp in range(len(stack)):
                px, py = stack.pop(0)
                if not rooms[px][py]:
                    return level

                if i - 1 > 0 and rooms[i - 1][j] != -1:
                    stack.append((i - 1, j))
                if i + 1 < m and rooms[i + 1][j] != -1:
                    stack.append((i + 1, j))
                if j - 1 > 0 and rooms[i - 1][j] != -1:
                    stack.append((i, j - 1))
                if j + 1 < n and rooms[i][j + 1] != -1:
                    stack.append((i, j + 1))

            level += 1

        return 0