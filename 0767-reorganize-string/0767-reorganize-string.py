class Solution:
    def reorganizeString(self, s: str) -> str:
        d = Counter(s)
        
        heap = [(-v,k) for k,v in d.items()]
        
        heapq.heapify(heap)
        alt = None
        res = ''
        
        while heap:
            c, k = heapq.heappop(heap)
            if c != 0:
                res += k
                c += 1

                if alt:
                    heapq.heappush(heap, alt) 
                alt = (c,k)

        if len(s) != len(res): return ''
        else: return res
                
            
            
            
            
            
            
            
        