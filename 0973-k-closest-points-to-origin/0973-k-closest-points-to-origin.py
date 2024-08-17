class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        
        for a, b in points:
            dist = a**2 + b**2
            heap.append([dist, a, b])
        
        heapq.heapify(heap)
        
        while k>0:
            d, a, b = heapq.heappop(heap)
            res.append([a,b])
            k -= 1
        
        return res