class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind()
        for i, j in stones:
            uf.union(i, ~j)

        return len(stones) - uf.component


class UnionFind():
    def __init__(self):
        self.uf = {}
        self.component = 0

    def union(self, a, b):
        if a not in self.uf and b not in self.uf:
            self.component += 1
        if a in self.uf and b in self.uf and not self.same(a, b):
            self.component -= 1

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
