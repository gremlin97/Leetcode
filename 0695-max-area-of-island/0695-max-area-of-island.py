class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        res = 0
        
        def dfs(r,c):
            curr = 0
            if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c] == 1:
                grid[r][c] = -1
                
                return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1) 
            else:
                return 0
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res,dfs(r,c))
        return res
                
                
        