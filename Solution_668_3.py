#TLE
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        h = []
        for i in range(1,m+1):
            for j in range(1,n+1):
                if len(h) < k:
                    heapq.heappush(h,-i*j)
                elif i*j <= -h[0]:
                    heapq.heappop(h)
                    heapq.heappush(h,-i*j)
        return -h[0]