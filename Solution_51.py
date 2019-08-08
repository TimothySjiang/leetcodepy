class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def couldPlace(i, j):
            if not i <= n - 1 or not j <= n - 1:
                return False

            if not rows[i] and not columns[j]:
                for p in visited:
                    if abs(i - p[0]) == abs(j - p[1]):
                        return False
                return True

        def remove(i, j):
            rows[i] = 0
            columns[j] = 0
            visited.remove((i, j))

        def placeNext(i, j, path):
            for t in range(0, j - 1):
                backtrack(i + 1, t, path)
            for t in range(j + 2, n):
                backtrack(i + 1, t, path)

        def backtrack(i, j, path):
            if couldPlace(i, j):
                rows[i] = 1
                columns[j] = 1
                visited.add((i, j))

                pos = "." * j + 'Q' + "." * (n - j - 1)

                if len(visited) == n:
                    nonlocal result
                    result.append(path + [pos])

                placeNext(i, j, path + [pos])
                remove(i, j)

        result = []
        rows = [0 for x in range(n)]
        columns = [0 for x in range(n)]
        visited = set()

        for j in range(n):
            backtrack(0, j, [])

        return result