class Solution(object):
    def removeStones(self, stones):

        N = len(stones)
        father = UnionFind(N)

        for i in range(N):
            for j in range(i + 1, N):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    father.connect(i, j)
        res = N
        for i in range(N):
            if father.father[i] == i:
                res -= 1
        return res


class UnionFind():
    def __init__(self, n):
        self.father = dict([(i, i) for i in range(n)])

    def find(self, node):
        path = []
        while node != self.father[node]:
            node = self.father[node]
        return node

    def query(self, a, b):
        return self.find(a) == self.find(b)

    def connect(self, a, b):
        self.father[self.find(a)] = self.find(b)