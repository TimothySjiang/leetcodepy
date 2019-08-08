class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        result =  sorted(intervals)
        for i in range(len(result)-1):
            if result[i][1] <= result[i+1][0]:
                continue
            else:
                return False
        return True