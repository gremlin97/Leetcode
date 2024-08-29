class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = {}
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                p = s[i:j+1]
                if p == p[::-1]:
                    res += 1

        return res
                
            
            