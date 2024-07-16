class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxp = ''
        for i in range(len(s)):
            for j in range(i, len(s)+1):
                p = s[i:j]
                if p and p == p[::-1] and len(p)>len(maxp):
                    maxp = p
        return maxp
                    
                
                
        