class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-x for x in stones]
        heapq.heapify(pq)
        while len(pq) > 1:
            x,y = -heapq.heappop(pq),-heapq.heappop(pq)
            smashed = - abs(x-y)
            if smashed:
                heapq.heappush(pq,smashed)
        return -pq[0] if pq else 0