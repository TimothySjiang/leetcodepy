class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        uf = UnionFind()
        n = len(row) // 2
        uf.size = n
        for i in range(n):
            u = row[2 * i] // 2
            v = row[2 * i + 1] // 2
            uf.union(u, v)

        return n - uf.size


class UnionFind():
    def __init__(self):
        self.uf = {}
        self.size = 0

    def connected(self, a, b):
        return self.find(a) == self.find(b)

    def union(self, a, b):
        self.uf.setdefault(a, a)
        self.uf.setdefault(b, b)
        if not self.connected(a, b):
            self.uf[self.find(a)] = self.find(b)
            self.size -= 1

    def find(self, node):
        path = []
        while node != self.uf[node]:
            path.append(node)
            node = self.uf[node]
        for n in path:
            self.uf[n] = node

        return node