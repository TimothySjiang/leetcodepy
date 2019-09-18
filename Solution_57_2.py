class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
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
            i+=1

        res.append([start,end])
        res += intervals[i:]
        return res