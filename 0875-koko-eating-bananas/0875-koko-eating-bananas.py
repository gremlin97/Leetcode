class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 3 6 7 11 - 8
        
        '''
        0 3 4 8
        0 0 0 4
        0 0 0 0
        
        '''
        
        def doSim(i):
            ch = 0
            for x in piles:
                ch = ch + math.ceil(x/i)
            if ch > h:
                return False
            else:
                return True
            
        i = 1
        min_res = float('inf')
        l, r = 1, max(piles)
        while l<=r:
            mid = l + (r-l)//2
            
            if doSim(mid):
                min_res = min(min_res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return min_res
                
                
        
        
        
        
        