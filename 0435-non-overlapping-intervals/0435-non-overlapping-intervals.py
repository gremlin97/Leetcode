class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        last_end = -float('inf')
        c = 0
        for s,e in intervals:
            if s >= last_end:
                last_end = e
                c += 1
        return len(intervals) - c
            
        