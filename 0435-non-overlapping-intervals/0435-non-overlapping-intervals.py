class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        last_end = -float('inf')
        
        
        # 1 2 - 2 3 - 1 3 - 3 4
        print(intervals)
        
        remove = 0
        
        for s, e in intervals:
            if s < last_end:
                remove += 1
            else:
                last_end = e
        
        return remove
        