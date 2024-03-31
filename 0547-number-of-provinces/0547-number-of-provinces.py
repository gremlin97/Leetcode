class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        seen = set()
        
        def dfs(ni):
            for j in range(len(isConnected)):
                if j not in seen and isConnected[ni][j] == 1:
                    seen.add(j)
                    dfs(j)
        
        for i in range(len(isConnected)):
            if i not in seen:
                dfs(i)
                res += 1
        
        return res
                
            
            
        