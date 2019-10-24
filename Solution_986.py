class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        p1 = 0
        p2 = 0
        res = []
        while p1 < len(A) and p2 < len(B):
            interval1 = A[p1]
            interval2 = B[p2]
            if interval1[1] >= interval2[0] and interval2[1] >= interval1[0]:
                start = max(interval1[0], interval2[0])
                end = min(interval1[1], interval2[1])
                res.append([start, end])
            if interval2[1] > interval1[1]:
                p1 += 1
            else:
                p2 += 1

        return res
