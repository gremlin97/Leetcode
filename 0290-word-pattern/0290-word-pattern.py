from collections import Counter

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        
        if len(s)!=len(pattern):
            return False
        
        hashmap = {}
        
        for p, w in zip(pattern, s):
            if (w in hashmap.values() and p not in hashmap.keys()) or (w not in hashmap.values() and p in hashmap.keys()):
                return False
            elif w in hashmap.values() and hashmap[p]!= w:
                return False
            else:
                hashmap[p] = w
        
        return True
            
        
            
        