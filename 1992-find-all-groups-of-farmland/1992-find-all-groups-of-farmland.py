class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res = []
        def dfs(r,c):
            x, y = r, c
            if 0<=r<len(land) and 0<=c<len(land[0]) and land[r][c] == 1:
                land[r][c] = -1
                directions = [[-1,0],[0,1],[1,0],[0,-1]]
                for a, b in directions:
                    xt, yt = dfs(r+a,c+b)
                    x = max(x, xt)
                    y = max(y, yt)
                return x, y
            return -1, -1
            
        
        for r in range(len(land)):
            for c in range(len(land[0])):
                if land[r][c] == 1:
                    x, y = dfs(r,c)
                    res.append([r, c, x, y])
        
        return res
                    
                
                
                
        