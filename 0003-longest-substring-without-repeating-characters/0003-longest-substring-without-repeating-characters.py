class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        visited  = set()
        res = 0
        for r in range(len(s)):
            # print(visited, res)
            if s[r] not in visited:
                visited.add(s[r])
                res = max(res, (r-l)+1)
                
            else:
                while s[r] in visited:
                    visited.remove(s[l])
                    l += 1
                visited.add(s[r])
        
        return res
            
        