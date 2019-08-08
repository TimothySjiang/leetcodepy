class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        return self.merge(sorted(intervals))

    def merge(self, intervals):
        merged = []
        for interval in intervals:
            if not merged:
                merged.append(interval)
            elif merged[-1][1] >= interval[0]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)
        return merged