class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        squares = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                if not board[i][j] == '.':
                    t = i // 3 * 3 + j // 3
                    if board[i][j] not in rows[i] and board[i][j] not in cols[j] and board[i][j] not in squares[t]:
                        rows[i].add(board[i][j])
                        cols[j].add(board[i][j])
                        squares[t].add(board[i][j])
                    else:
                        return False
        return True