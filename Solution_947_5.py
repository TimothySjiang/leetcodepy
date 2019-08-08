class Solution(object):
    def removeStones(self, stones):
        N = len(stones)
        father = UnionFind()

        for i, j in stones:
            father.union(i, ~j)

        res = N
        return res - len({father.find(x) for x in father.uf})


class UnionFind():
    def __init__(self):
        self.uf = {}

    def find(self, node):
        while node != self.uf[node]:
            node = self.uf[node]
        return node

    def same(self, a, b):
        return self.find(a) == self.find(b)

    def union(self, a, b):
        self.uf.setdefault(a, a)
        self.uf.setdefault(b, b)
        self.uf[self.find(a)] = self.find(b)