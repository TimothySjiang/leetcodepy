class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind()
        res = []
        board = [[0 for i in range(n)] for i in range(m)]

        def detect(i, j):
            if i < 0 or i > m - 1 or j < 0 or j > n - 1 or board[i][j] != 1:
                return None
            else:
                return (i, j)

        for i, j in positions:
            board[i][j] = 1
            uf.union((i, j), detect(i - 1, j))
            uf.union((i, j), detect(i + 1, j))
            uf.union((i, j), detect(i, j - 1))
            uf.union((i, j), detect(i, j + 1))
            res.append(len({uf.find(x) for x in uf.uf}))
        return res


class UnionFind:
    def __init__(self):
        self.uf = {}

    def same(self, a, b):
        return self.find(a) == self.find(b)

    def union(self, a, b):
        self.uf.setdefault(a, a)
        if not b:
            return None
        else:
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
