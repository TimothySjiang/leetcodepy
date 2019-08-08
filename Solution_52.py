class Solution:
    def totalNQueens(self, n: int) -> int:
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

        def placeNext(i, j):
            for t in range(0, i - 1):
                backtrack(t, j + 1)
            for t in range(i + 2, n):
                backtrack(t, j + 1)

        def backtrack(i, j):
            if couldPlace(i, j):
                rows[i] = 1
                columns[j] = 1
                visited.add((i, j))
                if len(visited) == n:
                    nonlocal count
                    count += 1
                placeNext(i, j)
                remove(i, j)

        count = 0
        rows = [0 for x in range(n)]
        columns = [0 for x in range(n)]
        visited = set()

        for i in range(n):
            backtrack(i, 0)

        return count