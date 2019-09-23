#BS
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        lo, hi = 1, m * n + 1
        while lo < hi:
            mi = (lo + hi) // 2
            count = self.enough(mi, m, n, k)
            if count >= k:
                hi = mi
            else:
                lo = mi + 1
        return lo

    def enough(self, x, m, n, k):
        count = 0
        for i in range(1, m + 1):
            count += min(x // i, n)
        return count
