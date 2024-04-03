class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 0
        last_end = -float('inf')
        points.sort(key = lambda x:x[1])
        for s,e in points:
            if s > last_end:
                last_end = e
                count += 1
        return count