class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        res = 0
        
        def dfs(r,c):
            curr = 0
            if 0<=r<len(grid) and 0<=c<len(grid[0]) and (r,c) not in visited and grid[r][c] == 1:
                visited.add((r,c))
                return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1) 
            else:
                return 0
            
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited:
                    res = max(res,dfs(r,c))
        return res
                
                
        