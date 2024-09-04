class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        
        d1 = Counter(s1)
        l = len(s1)
        
        #abc - dcda -> len(s2) - l = 4-3 = 1
        for i in range(len(s2)-l+1):
            # print(i+1, len(s2)-1)
            sub = s2[i:i+l]
            # print(sub)
            d2 = Counter(sub)
            
            if d1 == d2:
                return True
        
        return False
    
        