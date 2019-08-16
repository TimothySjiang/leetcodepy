class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []
        pacific, atlantic = set(), set()
        m, n = len(matrix), len(matrix[0])
        for i in range(n):
            self.dfs(0, i, matrix, pacific, 0)
            self.dfs(m - 1, i, matrix, atlantic, 0)
        for i in range(m):
            self.dfs(i, 0, matrix, pacific, -1)
            self.dfs(i, n - 1, matrix, atlantic, 0)
        return list(pacific & atlantic)

    def dfs(self, x, y, matrix, visit, height):
        m, n = len(matrix), len(matrix[0])
        if x < 0 or x >= m or y < 0 or y >= n or (x, y) in visit:
            return
        if matrix[x][y] < height:
            return
        visit.add((x, y))
        self.dfs(x - 1, y, matrix, visit, matrix[x][y])
        self.dfs(x + 1, y, matrix, visit, matrix[x][y])
        self.dfs(x, y - 1, matrix, visit, matrix[x][y])
        self.dfs(x, y + 1, matrix, visit, matrix[x][y])
