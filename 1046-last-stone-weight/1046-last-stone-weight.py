import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        _stones = stones
        _stones = [-x for x in _stones]
        heapq.heapify(_stones)
        
        while len(_stones)>1:
            l1 = heapq.heappop(_stones)
            l2 = heapq.heappop(_stones)
            
            if l1==l2:
                continue
            else:
                heapq.heappush(_stones, l1-l2)
        
        if _stones:
            return -heapq.heappop(_stones)
        else:
            return 0
            
            
        
        