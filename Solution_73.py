class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    self.walk(matrix, i, j)

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '#':
                    matrix[i][j] = 0

    def walk(self, matrix, i, j):
        m = len(matrix)
        n = len(matrix[0])
        for t in range(m):
            if matrix[t][j]:
                matrix[t][j] = '#'
        for t in range(n):
            if matrix[i][t]:
                matrix[i][t] = '#'

        return matrix