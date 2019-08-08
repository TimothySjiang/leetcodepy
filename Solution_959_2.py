class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        uf = UnionFind()
        for i in range(len(grid)):
            for j in range(len(grid)):
                if i:
                    uf.union((i - 1, j, 2), (i, j, 4))
                if j:
                    uf.union((i, j - 1, 3), (i, j, 1))
                if grid[i][j] != "/":
                    uf.union((i, j, 1), (i, j, 2))
                    uf.union((i, j, 3), (i, j, 4))
                if grid[i][j] != "\\":
                    uf.union((i, j, 2), (i, j, 3))
                    uf.union((i, j, 1), (i, j, 4))

        return len({uf.find(x) for x in uf.uf})


class UnionFind():
    def __init__(self):
        self.uf = {}

    def union(self, a, b):
        self.uf.setdefault(a, a)
        self.uf.setdefault(b, b)
        self.uf[self.find(a)] = self.find(b)

    def same(self, a, b):
        return self.find(a) == self.find(b)

    def find(self, node):
        path = []
        while node != self.uf[node]:
            path.append(node)
            node = self.uf[node]
        for n in path:
            self.uf[n] = node

        return node