from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = dict(Counter(ransomNote))
        c2 = dict(Counter(magazine))
        
        for x in ransomNote:
            if x not in c2:
                return False
            if x in c2:
                if c2[x] < c1[x]:
                    return False
        
        return True
        
        
        
        
        
        
        