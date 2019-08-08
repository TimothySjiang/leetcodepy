class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        N = len(stones)
        self.map = [-1] * N
        for i in range(N):
            for j in range(i + 1, N):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    self.union(i, j)
        res = N
        print(self.map)
        for i in range(N):
            if self.map[i] == -1:
                res -= 1
        return res

    def find(self, x):
        return x if self.map[x] == -1 else self.find(self.map[x])

    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            self.map[fx] = fy