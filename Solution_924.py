class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        m = len(graph)
        n = len(graph[0])
        uf = UnionFind()

        for i in range(m):
            for j in range(n):
                if graph[i][j] == 1:
                    uf.union(i, j)

        initial.sort()
        MAX = -1
        for i in initial:
            count = 0
            for j in range(m):
                if uf.find(i) == uf.find(j):
                    count += 1
            if count > MAX:
                MAX = count
                res = i

        return res


class UnionFind():
    def __init__(self):
        self.uf = {}

    def connected(self, a, b):
        return self.find(a) == self.find(b)

    def union(self, a, b):
        self.uf.setdefault(a, a)
        self.uf.setdefault(b, b)

        self.uf[self.find(a)] = self.find(b)

    def find(self, node):
        path = []
        while node != self.uf[node]:
            path.append(node)
            node = self.uf[node]
        for n in path:
            self.uf[n] = node

        return node