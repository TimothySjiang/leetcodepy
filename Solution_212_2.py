class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                if letter not in node:
                    node[letter] = {}
                node = node[letter]
            node[WORD_KEY] = word

        rowNum = len(board)
        colNum = len(board[0])
        matchedWords = []

        for row in range(rowNum):
            for col in range(colNum):
                if board[row][col] in trie:
                    self.backtracking(board, row, col, trie, matchedWords)

        return matchedWords

    def backtracking(self, board, row, col, parent, matchedWords):
        WORD_KEY = '$'
        letter = board[row][col]
        currNode = parent[letter]
        rowNum = len(board)
        colNum = len(board[0])

        word_match = currNode.pop(WORD_KEY, False)
        if word_match:
            matchedWords.append(word_match)

        board[row][col] = '#'
        for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            newRow, newCol = row + rowOffset, col + colOffset
            if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                continue
            if not board[newRow][newCol] in currNode:
                continue
            self.backtracking(board, newRow, newCol, currNode, matchedWords)
        board[row][col] = letter

        if not currNode:
            parent.pop(letter)