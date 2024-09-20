class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        d = {}
        res = 0
        for r in range(len(s)):

            if s[r] not in d:
                d[s[r]] = 1
            else:
                d[s[r]] += 1
            
            if (r-l+1) - max(list(d.values())) > k:
                d[s[l]] -= 1
                l += 1
            else:
                res = max(res, r-l+1)
            # print(s[l:r+1], res)
        return res
                
        