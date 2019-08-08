class Solution:
    def longestMountain(self, A: List[int]) -> int:
        up, down = [0] * len(A), [0] * len(A)
        for i in range(1, len(A)):
            if A[i] > A[i - 1]: up[i] = up[i - 1] + 1
        for i in range(len(A) - 2, -1, -1):
            if A[i] > A[i + 1]: down[i] = down[i + 1] + 1

        res = 0
        for i in range(len(A)):
            if up[i] and down[i]:
                res = max(res, up[i] + down[i] + 1)
        return res