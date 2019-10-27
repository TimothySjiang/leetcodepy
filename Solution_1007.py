class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        candidate = set([A[0],B[0]])
        for i in range(1,len(A)):
            candidate &= set([A[i],B[i]])
            if not candidate: return -1
        c = candidate.pop()
        c1 = sum([x==c for x in A])
        c2 = sum([x==c for x in B])
        return len(A) - max(c1,c2)