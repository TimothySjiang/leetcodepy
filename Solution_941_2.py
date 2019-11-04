class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        i, N = 0, len(A)
        while i + 1 < N and A[i] < A[i + 1]:
            i += 1
        if i == 0 or i == N - 1:
            return False

        while i + 1 < N and A[i] > A[i + 1]:
            i += 1

        return i == N - 1