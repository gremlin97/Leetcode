class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # if len(s) ==  1 and s in wordDict: return True
        
        memo = {}
    
        def build(i):
            
            if i == len(s):
                return True
            
            if i in memo:
                return memo[i]
            
            for e in range(i, len(s)):
                if s[i:e+1] in wordDict:
                    if build(e+1):
                        memo[i] = True
                        return True
            memo[i] = False
        
        return build(0)
                    
                    
                