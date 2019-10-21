class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        if len(A) <= 1:
            return -1
        A.sort()
        p1 = 0
        p2 = len(A)-1
        res = float('-inf')
        while p1 < p2:
            if A[p1] + A[p2] < K:
                res = max(res,A[p1]+A[p2])
                p1 += 1
            else:
                p2 -= 1
        return res if res != float('-inf') else -1