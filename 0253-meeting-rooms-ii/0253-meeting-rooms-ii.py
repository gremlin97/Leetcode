class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        rooms = []
        rooms.append(intervals[0][1])
        heapq.heapify(rooms)
        # 2-4 7-10  h = [4], s=7
        for s,e in intervals[1:]:
            if s >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, e)
        return len(rooms)
            
        