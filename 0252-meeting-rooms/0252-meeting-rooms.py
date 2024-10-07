class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        
        # 5 10 - 15 20 - 0 30
        intervals.sort(key = lambda x: x[1])
        end_old = intervals[0][1]

        for s, e in intervals[1:]:
            print(s, end_old)
            if s < end_old:
                return False
            end_old = e
        return True

                
            
            