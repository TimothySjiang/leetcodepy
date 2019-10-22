"""
# Definition for an Interval.
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def employeeFreeTime(self, schedule: 'list<list<Interval>>') -> 'list<Interval>':
        h = []
        for i, intervals in enumerate(schedule):
            for interval in intervals:
                h.append((interval.start, interval.end, i, interval))
        heapq.heapify(h)
        intervals = []
        while h:
            interval = heapq.heappop(h)[3]
            if intervals and intervals[-1].end >= interval.start:
                intervals[-1].end = max(intervals[-1].end, interval.end)
            else:
                intervals.append(interval)

        res = []
        for i in range(len(intervals) - 1):
            res.append(Interval(intervals[i].end, intervals[i + 1].start))

        return res