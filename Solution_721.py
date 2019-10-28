#There some bug
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


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        dic = {}
        for account in accounts:
            newComponent = True
            if account[1] in uf.uf:
                newComponent = False
            uf.uf.setdefault(account[1], account[1])
            for i in range(1, len(account) - 1):
                if account[i + 1] in uf.uf:
                    newComponent = False
                uf.union(account[i], account[i + 1])
            if newComponent:
                dic[account[1]] = account[0]

        res = []
        for component in dic:
            merged = [dic[component]]
            for x in uf.uf:
                if uf.same(component, x):
                    merged.append(x)
            res.append(sorted(merged))

        return res
