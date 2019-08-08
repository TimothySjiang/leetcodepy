class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges: return None
        uf = UnionFind(len(edges))
        for first, second in edges:
            if not uf.query(first, second):
                uf.connect(first, second)
            else:
                return [first, second]
        return None


class UnionFind(object):
    def __init__(self, n):
        self.father = dict([(i, i) for i in range(1, n + 1)])

    def find(self, node):
        path = []
        while node != self.father[node]:
            path.append(node)
            node = self.father[node]
        for n in path:
            self.father[n] = node

        return node

    def query(self, a, b):
        return self.find(a) == self.find(b)

    def connect(self, a, b):
        self.father[self.find(a)] = self.find(b)   