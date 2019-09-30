class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        queue = [1]
        level = 0
        visited = set()
        visited.add(1)
        while queue:
            for i in range(len(queue)):
                v = queue.pop(0)
                if v == n * n:
                    return level
                for j in range(1, 7):
                    if v + j not in visited and v + j <= n * n:
                        x, y = self.pos(v + j, n)
                        if board[x][y] != -1:
                            if board[x][y] not in visited:
                                queue.append(board[x][y])
                        else:
                            visited.add(v + j)
                            queue.append(v + j)

            level += 1
        return -1

    def pos(self, val, n):
        x = n - 1 - (val - 1) // n
        if not (val - 1) // n % 2:
            y = (val - 1) - (n - 1 - x) * n
        else:
            y = -val + (n - 1 - x) * n
        return x, y