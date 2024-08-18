class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        last = -1
        intervals.sort(key = lambda x:x[0])
        for s,e in intervals:
            if s>=last:
                last = e
            else:
                return False
        return True
            
        