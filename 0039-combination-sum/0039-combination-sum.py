class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subsets = []
        
        def recur(i, t):
            #print(subsets, res, t, i)
            if t == target:
                res.append(subsets.copy())
                return
            
            if i == len(candidates):
                return
            
            if t > target:
                return
            
            subsets.append(candidates[i])
            t += candidates[i]
            recur(i, t)
            
            subsets.pop()
            t -= candidates[i]
            recur(i+1, t)
            
        recur(0,0)
        return res
            
        