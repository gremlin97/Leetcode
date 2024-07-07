class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            s1 = 1
            if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c] == 1:
                grid[r][c] = -1
                
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                
                for a,b in directions:
                    s1 += dfs(r+a, c+b) 
                
                return s1
            
            else:
                return 0
        
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        
        print(grid)
        
        return res
                    