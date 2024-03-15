class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = []
                d[s[i]].append(i)
            else:
                d[s[i]].append(i)
                
        e = {}
        for i in range(len(t)):
            if t[i] not in e:
                e[t[i]] = []
                e[t[i]].append(i)
            else:
                e[t[i]].append(i)
        
        if list(e.values()) == list(d.values()):
            return True
        return False
            
                
                
        