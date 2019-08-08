class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        uf = UnionFind()
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    uf.union(i, j)

        return len({uf.find(x) for x in uf.uf})


class UnionFind():
    def __init__(self):
        self.uf = {}

    def union(self, a, b):
        self.uf.setdefault(a, a)
        self.uf.setdefault(b, b)
        self.uf[self.find(a)] = self.find(b)

    def same(self, a, b):
        return self.uf.find(a) == self.uf.find(b)

    def find(self, node):
        path = []
        while node != self.uf[node]:
            path.append(node)
            node = self.uf[node]
        for n in path:
            self.uf[n] = node
        return node