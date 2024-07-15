class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        comb = []
        for i in range(len(s)):
            for j in range(i, len(s)+1):
                p = s[i:j]
                if p == p[::-1] and p:
                    res += 1
#                     comb.append(p)
        
#         print(comb)
        return res
                
            
            