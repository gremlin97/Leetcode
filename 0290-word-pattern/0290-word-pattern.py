from collections import Counter

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        
        if len(pattern) != len(s):
            return False
        
        hashmap = {}
        
        for c, w in zip(pattern, s):
            if c in hashmap:
                if hashmap[c]!=w:
                    return False
            elif w in hashmap.values():
                return False
            else:
                hashmap[c]=w
        return True
#         for x in s:
#             if x in hashmap:
#                 hashmap[x] += 1
#             else:
#                 hashmap[x] = 1
        
#         print(hashmap)
        
#         a = hashmap.values()
        
#         b = dict(Counter(pattern))
#         b = b.values()
        
#         print(a,b)
        
#         if list(a) == list(b):
#             return True
#         else:
#             return False
            
        
            
        