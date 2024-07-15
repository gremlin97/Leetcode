class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)+1):
                p = s[i:j]
                if p == p[::-1] and p:
                    res += 1

        return res
                
            
            