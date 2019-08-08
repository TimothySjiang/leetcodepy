class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def transform(i, j):
            count = 0
            if i - 1 >= 0:                          count += board[i - 1][j] % 2
            if i - 1 >= 0 and j + 1 <= column - 1:       count += board[i - 1][j + 1] % 2
            if i - 1 >= 0 and j - 1 >= 0:              count += board[i - 1][j - 1] % 2
            if j + 1 <= column - 1:                  count += board[i][j + 1] % 2
            if j - 1 >= 0:                         count += board[i][j - 1] % 2
            if i + 1 <= row - 1:                     count += board[i + 1][j] % 2
            if i + 1 <= row - 1 and j + 1 <= column - 1:  count += board[i + 1][j + 1] % 2
            if i + 1 <= row - 1 and j - 1 >= 0:         count += board[i + 1][j - 1] % 2

            return count

        row = len(board)
        column = len(board[0])

        for i in range(row):
            for j in range(column):
                if not board[i][j] % 2:
                    if transform(i, j) == 3:
                        board[i][j] = 2
                else:
                    indi = transform(i, j)
                    if indi < 2:
                        board[i][j] = 3
                    if indi > 3:
                        board[i][j] = 3

        for i in range(row):
            for j in range(column):
                if board[i][j] == 2:  board[i][j] = 1
                if board[i][j] == 3:  board[i][j] = 0    