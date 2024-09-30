class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        res = ''
        
        mem = []
        
        for i in range(len(s)):
            mem.append([-1] * len(s))
            
        def recur(i,j):
            if i>=j:
                return True
            
            elif mem[i][j]!= -1:
                return mem[i][j]
            
            elif s[i] == s[j]:
                mem[i][j] = recur(i+1,j-1)
                return mem[i][j]
            else:
                mem[i][j] = False
                return mem[i][j]          
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if recur(i,j) and j-i+1 > max_len:
                    max_len = j-i+1
                    res = s[i:j+1]
        return res
    
    
                
        