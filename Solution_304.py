class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix: return
        m = len(matrix)
        n = len(matrix[0])
        self.dp = [[0] * (n + 1) for i in range(m)]
        for i in range(m):
            for j in range(1, n + 1):
                self.dp[i][j] += self.dp[i][j - 1] + matrix[i][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2 + 1):
            res += self.dp[i][col2 + 1] - self.dp[i][col1]
        return res


        # Your NumMatrix object will be instantiated and called as such:
        # obj = NumMatrix(matrix)
        # param_1 = obj.sumRegion(row1,col1,row2,col2)