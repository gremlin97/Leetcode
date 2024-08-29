class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        res = []
        
        last_start = intervals[0][0]
        last_end = intervals[0][1]
        
        for s,e in intervals[1:]:
            if s> last_end:
                res.append([last_start, last_end])
                last_start = s
                last_end = e
            else:
                last_start = min(s, last_start)
                last_end = max(e, last_end)
                
        res.append([last_start, last_end])
        return res
        