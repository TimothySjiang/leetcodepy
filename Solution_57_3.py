#Practice
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l = 0
        r = len(intervals)
        while l < r:
            mid = l + (r - l) // 2
            if intervals[mid] < newInterval:
                l = mid + 1
            else:
                r = mid
        print(l)
        if l == 0:
            start = newInterval[0]
            end = newInterval[1]
            i = 0
            while i < len(intervals):
                if end >= intervals[i][0]:
                    start = min(start, intervals[i][0])
                    end = max(end, intervals[i][1])
                else:
                    break
                i += 1
            return [[start, end]] + intervals[i:]

        if l == len(intervals):
            start = newInterval[0]
            end = newInterval[1]
            if start <= intervals[-1][1]:
                start = min(start, intervals[-1][0])
                end = max(end, intervals[-1][1])
                return intervals[:-1] + [[start, end]]
            return intervals + [[start, end]]

        start = newInterval[0]
        end = newInterval[1]
        if start <= intervals[l - 1][1]:
            start = min(start, intervals[l - 1][0])
            end = max(end, intervals[l - 1][1])
            nl = l

            while nl < len(intervals):
                if end >= intervals[nl][0]:
                    start = min(start, intervals[nl][0])
                    end = max(end, intervals[nl][1])
                else:
                    break
                nl += 1
            return intervals[:l - 1] + [[start, end]] + intervals[nl:]
        else:
            nl = l
            while nl < len(intervals):
                if end >= intervals[nl][0]:
                    start = min(start, intervals[nl][0])
                    end = max(end, intervals[nl][1])
                else:
                    break
                nl += 1
            return intervals[:l] + [[start, end]] + intervals[nl:]