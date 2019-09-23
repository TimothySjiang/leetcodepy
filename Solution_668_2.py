#MLE
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        h = []
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                h.append(i * j)
        heapq.heapify(h)
        for i in range(k):
            res = heapq.heappop(h)
        return res
