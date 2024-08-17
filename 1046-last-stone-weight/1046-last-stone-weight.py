class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        
        while len(heap)>1:
            f = heapq.heappop(heap)
            s = heapq.heappop(heap)
            f-s
            if s>f:
                heapq.heappush(heap, f - s)
        
        if heap:
            return abs(heap[0])
        return 0
        