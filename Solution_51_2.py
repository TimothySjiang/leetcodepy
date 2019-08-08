class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        visited = set()
        self.recursion(n, visited, [], results)
        return results

    def recursion(self, n, visited, result, results):
        if len(result) == n:
            results.append(result)
            return

        for i in range(n):
            if self.valid(visited, i, len(result)):
                visited.add((i, len(result)))
                pos = '.' * i + 'Q' + '.' * (n - i - 1)
                self.recursion(n, visited, result + [pos], results)
                self.remove(visited, i, len(result))

    def valid(self, visited, x, y):
        for p in visited:
            if abs(x - p[0]) == abs(y - p[1]) or x == p[0] or y == p[1]:
                return False

        return True

    def remove(self, visited, x, y):
        visited.remove((x, y))