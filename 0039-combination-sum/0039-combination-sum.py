class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        subs = []
        
        def recur(i, s):
            if s == 0:
                res.append(subs[::])
                return
            
            elif s < 0:
                return
            
            elif i == len(candidates):
                return 
            
            subs.append(candidates[i])
            s -= candidates[i]
            recur(i, s)
            
            subs.pop()
            s += candidates[i]
            recur(i+1, s)
            
            return
        
        recur(0,target)
        return res