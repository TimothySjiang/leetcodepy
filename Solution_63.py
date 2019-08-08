class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[-1][-1] :
            return 0
        for i in range(m):
            for j in range(n):
                if not i and not j:
                     obstacleGrid[i][j] = 1
                else:
                    if obstacleGrid[i][j]==1:
                        obstacleGrid[i][j] = -1
                    else:
                        obstacleGrid[i][j] += self.helpCount(obstacleGrid, i - 1, j) + self.helpCount(obstacleGrid, i, j - 1)

        return obstacleGrid[-1][-1]

    def helpCount(self, count, i, j):
        if not count or i < 0 or j < 0 or count[i][j]==-1:
            return 0
        else:
            return count[i][j]