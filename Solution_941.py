class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3: return False
        p1, p2 = 0, len(A) - 1
        while p1 < p2 and A[p1] < A[p1 + 1]:
            p1 += 1
        while p2 > p1 and A[p2] < A[p2 - 1]:
            p2 -= 1

        if p1 == p2 and p1 > 0 and p2 < len(A) - 1:
            return True
        return False