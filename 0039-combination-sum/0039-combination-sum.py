class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        subsets = []
        res = []
        
        def recur(i, t):
            #print(subsets, res)
            if i == len(candidates):
                if t == target:
                    res.append(subsets.copy())
                return
            
            if t>target:
                return
            
            subsets.append(candidates[i])
            t += candidates[i]
            recur(i, t)
            
            subsets.pop()
            t -= candidates[i]
            recur(i+1, t)
        
        recur(0, 0)
        print(res)
        return res
            
            
        