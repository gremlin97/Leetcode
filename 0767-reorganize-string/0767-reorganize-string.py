class Solution:
    def reorganizeString(self, s: str) -> str:
        d = Counter(s)
        
        heap = [[-v,k] for k,v in d.items()]
        heapq.heapify(heap)
        alt = None
        res = ''
        #print(heap)
        
        # aab - a, prev - a --> ab ,prev b
        
        while heap:
            c, k = heapq.heappop(heap)
            # print(k,c, heap, alt)
            if c != 0:
                res += k
                c += 1

                if alt:
                    heapq.heappush(heap, alt)
                # ab - prev - a > b -> a  
                alt = [c,k]
                
        # print('Result',res)
           
        if len(s) != len(res): return ''
        else: return res
                
            
            
            
            
            
            
            
        