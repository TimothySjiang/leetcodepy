#Slow
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        res1 = [0] * (len(A)-1)
        res2 = [0] * (len(A)-1)
        for i in range(len(A)-1):
            if A[i] <= A[i+1]:
                res1[i] = True
            if A[i] >= A[i+1]:
                res2[i] = True
        if sum(res1) == len(res1) or sum(res2) == len(res2):
            return True
        return False