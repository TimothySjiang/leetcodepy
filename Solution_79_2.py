class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word: return False
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if self.recursion(board, i, j, word, 1, visited):
                        return True
                    visited.remove((i, j))
        return False

    def recursion(self, board, i, j, word, pos, visited):
        if pos == len(word):
            return True
        for x, y in [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= x <= len(board) - 1 and 0 <= y <= len(board[0]) - 1 and board[x][y] == word[pos] and (
            x, y) not in visited:
                visited.add((x, y))
                if self.recursion(board, x, y, word, pos + 1, visited):
                    return True
                visited.remove((x, y))
        return False
