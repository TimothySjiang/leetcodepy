class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        if not A: return []
        m = len(A)
        n = len(A[0])
        res = [[0] * m for i in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][i] = A[i][j]

        return res