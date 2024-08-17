class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        
        while len(heap)>1:
            f = heapq.heappop(heap)
            s = heapq.heappop(heap)
            
            if f>s:
                left = s - f
                print(f,s,left)
                heapq.heappush(heap, left)
            else:
                left = f - s
                heapq.heappush(heap, left)
        
        if heap:
            return abs(heap[0])
        return 0
        