class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return
        m = len(board)
        n = len(board[0])

        def bfs(board, root):
            stack = [root]
            union = []
            while stack:
                i, j = stack.pop()
                if i < 0 or i > m - 1 or j < 0 or j > n - 1 or board[i][j] != 'O':
                    continue
                else:
                    board[i][j] = 'S'
                    stack.append((i - 1, j))
                    stack.append((i + 1, j))
                    stack.append((i, j - 1))
                    stack.append((i, j + 1))

        for i in [0, m - 1]:
            for j in range(n):
                bfs(board, (i, j))

        for i in range(m):
            for j in [0, n - 1]:
                bfs(board, (i, j))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == "S":
                    board[i][j] = 'O'

