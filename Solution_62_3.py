class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = [[0]*(n+1) for j in range(m+1)]
        count[1][1] = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                count[i][j] += count[i-1][j] + count[i][j-1]

        return count[-1][-1]
