class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subs = []
        candidates.sort()
        
        def recur(i, s):
            
            if s == 0:
                res.append(subs[::])
                return
            
            elif i == len(candidates) or s < 0:
                return 
            
            subs.append(candidates[i])
            s -= candidates[i]
            recur(i+1, s)
            
            subs.pop()
          
            
            while i<len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            
            s +=  candidates[i]
            recur(i+1, s)
            
            return
        
        recur(0, target)
        return res