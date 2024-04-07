class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        alp = list(string.ascii_lowercase)
        res = ''
        
        def mindis(c1,c2):
            return min((ord(c1) - ord(c2))%26, (ord(c2) - ord(c1))%26)
        
        for c in s:
            for l in alp:
                if k - mindis(c,l) >= 0:
                    k -= mindis(c,l)
                    res += l
                    break
        
        return res
                    
                
        

        