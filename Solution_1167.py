class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        h = []
        for stick in sticks:
            h.append(stick)
        heapq.heapify(h)
        count = 0
        while len(h) > 1:
            newstick = heapq.heappop(h) + heapq.heappop(h)
            count += newstick
            heapq.heappush(h,newstick)
        return count