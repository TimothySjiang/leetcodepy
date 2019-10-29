class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        res = 0
        equal = 0
        for i in range(len(A)-1):
            if A[i] < A[i+1]:
                res += 1
            elif A[i] > A[i+1]:
                res -= 1
            else:
                equal += 1
        return abs(res)+equal == len(A)-1