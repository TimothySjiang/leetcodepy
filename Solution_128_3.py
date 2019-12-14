class UF():
    def __init__(self):
        self.uf = {}

    def union(self, a, b):
        self.uf[self.find(a)] = self.find(b)

    def find(self, node):
        path = []
        while self.uf[node] != node:
            path.append(node)
            node = self.uf[node]
        res = node
        while node in path:
            self.uf[node] = res
        return res


class Solution:
    def longestConsecutive(self, num):
        num = list(set(num))
        uf = UF()
        for n in num:
            uf.uf.setdefault(n, n)
            if n - 1 in uf.uf:
                uf.union(n, n - 1)
            if n + 1 in uf.uf:
                uf.union(n, n + 1)
        count = collections.Counter([uf.find(x) for x in num])
        return max(count.values(), default=0)


