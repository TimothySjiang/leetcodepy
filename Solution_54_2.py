class Solution:
    def spiralOrder(self, matrix):
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        dx, dy = 0, 1
        result = []
        visited = set()
        while len(result) < m * n:
            result.append(matrix[i][j])
            visited.add(matrix[i][j])
            if matrix[(i + dx) % m][(j + dy) % n] in visited:
                dx, dy = dy, -dx
            i += dx
            j += dy
        return result
