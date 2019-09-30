#TLE
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []
        for word in words:
            found = False
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word[0]:
                        board[i][j] = '#'
                        if self.dfs(word, i, j, 1, board):
                            found = True
                            result.append(word)
                            board[i][j] = word[0]
                            break
                        board[i][j] = word[0]
                if found:
                    break
        return result

    def dfs(self, word, i, j, pos, board):
        if len(word) == pos:
            return True
        for x, y in [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= x <= len(board) - 1 and 0 <= y <= len(board[0]) - 1 and board[x][y] == word[pos]:
                board[x][y] = '#'
                if self.dfs(word, x, y, pos + 1, board):
                    board[x][y] = word[pos]
                    return True
                board[x][y] = word[pos]
        return False