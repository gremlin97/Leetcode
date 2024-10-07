class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        curr_area = 0
        
        d = [[0,1],[0,-1],[1,0],[-1,0]]
        
        res = 0
        
        def dfs(r,c):
            nonlocal curr_area
            if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c] == 1:
                grid[r][c] = -1
                
                for a, b in d:
                    if dfs(r+a, c+b):
                        curr_area += 1
                
                return True
            else:
                return False
            
        
        for r in range(rows):
            for c in range(cols):
                curr_area = 0
                if grid[r][c] == 1:
                    curr_area += 1
                    dfs(r,c)
                res = max(res, curr_area) 
        return res
                
                
        