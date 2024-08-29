class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        last_end = intervals[0][1]
        last_start = intervals[0][0]
        res = []
        
        for s,e in intervals[1:]:
            if last_end < s:
                res.append([last_start,last_end])
                last_end = e
                last_start = s
            else:
                if last_end >= s:
                    last_end = max(last_end, e)
                    last_start = min(last_start, s)
        res.append([last_start, last_end])
        return res
                    
                
                
        