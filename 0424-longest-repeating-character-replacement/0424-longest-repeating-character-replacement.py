class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, count = 0, {}
        res = 0
        
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1
            
            #abcd l = 0, r = 3,  r-l+1
            diff = (r-l+1) - max(count.values())
            if diff > k:
                count[s[l]] -= 1
                l+=1
            else:
                res = max(res, (r-l+1))
        
        return res
                
            
        
        