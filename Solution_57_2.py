class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        start = newInterval[0]
        end = newInterval[1]
        res = []
        i = 0
        while i < len(intervals):
            if start <= intervals[i][1]:
                if end < intervals[i][0]:
                    break
                start = min(start,intervals[i][0])
                end = max(end,intervals[i][1])
            else:
                res.append(intervals[i])
            i += 1

        res.append([start,end])
        res += intervals[i:]
        return res



