class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        x = []
        y = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    x.append(i)
                    y.append(j)
        res = 0
        medianx = self.median(x)
        mediany = self.median(y)
        for i in range(len(x)):
            res += abs(x[i] - medianx) + abs(y[i] - mediany)
        return int(res)

    def median(self, arr):
        l = len(arr)
        arr.sort()
        if l % 2:
            return arr[l // 2]
        else:
            return (arr[l // 2] + arr[l // 2 - 1]) / 2
