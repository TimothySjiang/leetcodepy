class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        h = []
        room = 0
        for s in intervals:
            if not len(h):
                heapq.heappush(h, (s[1], s))
                room += 1
                continue
            end = h[0][0]
            if end <= s[0]:
                heapq.heappop(h)
                heapq.heappush(h, (s[1], s))
            else:
                room += 1
                heapq.heappush(h, (s[1], s))
                continue

        return room