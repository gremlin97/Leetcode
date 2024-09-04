class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        visited = set()
        ml = 0
        
        for r in range(len(s)):
            if s[r] in visited:
                while s[r] in visited:
                    visited.remove(s[l])
                    l += 1
                    
            visited.add(s[r])
            cl = r-l+1
            ml = max(ml, cl)
            
        return ml
        
    # s = {w,k,e}
    #pwwkew -> wke
    
        
            
        