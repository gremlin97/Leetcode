class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x:x[1])
        last_end = -float('inf')
        for s,e in intervals:
            if s >= last_end:
                last_end = e
            else:
                return False
        return True
        