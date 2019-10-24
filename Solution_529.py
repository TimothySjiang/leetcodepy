class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
        if board[x][y] == 'E':
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx or dy:
                        newx = x + dx
                        newy = y + dy
                        if 0 <= newx < len(board) and 0 <= newy < len(board[0]):
                            if board[newx][newy] == 'M':
                                count += 1
            if count:
                board[x][y] = str(count)
            else:
                board[x][y] = 'B'
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx or dy:
                            newx = x + dx
                            newy = y + dy
                            if 0 <= newx < len(board) and 0 <= newy < len(board[0]) and board[newx][newy] == 'E':
                                self.updateBoard(board, [newx, newy])
        return board

