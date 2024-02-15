class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [x for x in range(1, n+1)]
        res = []
        subsets = []
        
        def dfs(i):
            if i>=len(arr):
                if len(subsets.copy()) == k:
                    res.append(subsets.copy())
                return
            
            subsets.append(arr[i])
            dfs(i+1)
            
            subsets.pop()
            dfs(i+1)
            
        dfs(0)
        
        return res
            
        