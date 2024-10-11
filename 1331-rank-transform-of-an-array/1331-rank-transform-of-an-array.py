class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr: return arr
        d = {}
        sorted_arr = sorted(arr)
        d[sorted_arr[0]] = 1
            
        prev = sorted_arr[0]
        rank = 1
        for x in sorted_arr[1:]:
           
            if prev != x:
                rank += 1
                
            prev = x    
            d[x] = rank
        
        res = []
        
        for x in arr:
            res.append(d[x])
        return res
        
            
            