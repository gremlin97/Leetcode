class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        
        d1 = Counter(s1)
        k = len(s1)
        d2 = Counter(s2[:k])
        
        if d1 == d2:
            return True

        l = 0
        for r in range(k, len(s2)):
            
            if d2[s2[l]] == 1:
                del d2[s2[l]]
            else:
                d2[s2[l]] -= 1
            
            if s2[r] in d2:
                d2[s2[r]] += 1
            else:
                d2[s2[r]] = 1
    
            if d1 == d2:
                return True
            l+=1
        
        return False
    
        