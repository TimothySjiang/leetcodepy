class Solution:
    def nthUglyNumber(self, n: int) -> int:
        h = []
        heapq.heappush(h, 1)
        i = 1
        while i <= n:
            r = heapq.heappop(h)
            if not r * 2 in h:
                heapq.heappush(h, r * 2)

            if not r * 3 in h:
                heapq.heappush(h, r * 3)

            if not r * 5 in h:
                heapq.heappush(h, r * 5)

            i = i + 1

        return r