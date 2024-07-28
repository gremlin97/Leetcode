class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        candidates.sort( )
        
        def recur(i, t):
            # print(res, curr, target, t)
            if i == len(candidates):
                if t == target:
                    res.append(curr[::])
                return
            
            if t>target:
                return
            
            curr.append(candidates[i])
            t += candidates[i]
            recur(i+1, t)
            curr.pop()
            t -= candidates[i]
            
            while i<len(candidates)-1 and candidates[i] == candidates[i+1]:
                i+=1
            recur(i+1, t)
        
        recur(0, 0)
        return res
            
        

        