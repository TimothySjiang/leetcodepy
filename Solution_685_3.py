class DSU:
    def __init__(self, N):
        self.ranks = [0] * (N + 1)
        self.groups = list(range(N + 1))

    def find(self, x):
        if self.groups[x] == x:
            return x
        return self.find(self.groups[x])

    def union(self, x, y):
        gx = self.find(x)
        gy = self.find(y)
        if gx == gy:
            return False
        if self.ranks[gx] > self.ranks[gy]:
            self.groups[gy] = gx
        elif self.ranks[gx] < self.ranks[gy]:
            self.groups[gx] = gy
        else:
            self.groups[gy] = gx
            self.ranks[gy] += 1
        return True


class Solution:
    def findRedundantDirectedConnection(self, edges):
        def is_cycle(edge):
            """
                return True if from edge=x, y can get back to x
            """
            x, y = edge
            while x != y and x in parent:
                x = parent[x]
            return x == y

        parent = {}
        candidates = []
        for x, y in edges:
            if y not in parent:
                parent[y] = x
            else:
                candidates.append([parent[y], y])
                candidates.append([x, y])

        if candidates:
            if is_cycle(candidates[0]):
                return candidates[0]
            return candidates[1]

        else:
            N = len(edges)
            dsu = DSU(N)
            for x, y in edges:
                if not dsu.union(x, y):
                    return [x, y]
        return []