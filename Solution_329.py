class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        memo = {}
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, self.dfs(matrix, i, j, memo))
        return res

    def dfs(self, matrix, x, y, memo):
        if (x, y) in memo:
            return memo[(x, y)]
        res = 1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            newx = x + dx
            newy = y + dy
            if 0 <= newx < len(matrix) and 0 <= newy < len(matrix[0]) and matrix[newx][newy] > matrix[x][y]:
                res = max(res, 1 + self.dfs(matrix, newx, newy, memo))

        memo[(x, y)] = res
        return memo[(x, y)]