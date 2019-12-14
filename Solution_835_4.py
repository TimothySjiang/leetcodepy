#Too Slow
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        N = len(A)
        count = collections.Counter()
        for i1 in range(N):
            for j1 in range(N):
                for i2 in range(N):
                    for j2 in range(N):
                            if A[i1][j1] and B[i2][j2]:
                                count[i1-i2, j1-j2] += 1
        return max(count.values(),default = 0)