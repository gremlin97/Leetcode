class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for s,e in intervals:
            if e < newInterval[0]:
                res.append([s,e])
            elif newInterval[1] < s:
                res.append(newInterval)
                newInterval = [s,e]
            else:
                newInterval[0] = min(newInterval[0], s)
                newInterval[1] = max(newInterval[1], e)
        res.append([newInterval[0], newInterval[1]])
        return res
        