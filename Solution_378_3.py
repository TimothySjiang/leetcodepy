class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = matrix[0][0]
        r = matrix[-1][-1]
        while l < r:
            m = l + (r - l) // 2
            total = 0
            for row in matrix:
                total += self.upperBound(row, m)
            if total >= k:
                r = m
            else:
                l = m + 1
        return l

    def upperBound(self, row, val):
        l = 0
        r = len(row)

        while l < r:
            m = l + (r - l) // 2
            if row[m] > val:
                r = m
            else:
                l = m + 1
        return l