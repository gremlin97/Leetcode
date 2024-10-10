class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # if len(s) ==  1 and s in wordDict: return True
        
        @lru_cache()
        def build(i):
            
            if i == len(s):
                return True
            
            for e in range(i, len(s)):
                if s[i:e+1] in wordDict:
                    if build(e+1):
                        return True
        
        return build(0)
                    
                    
                