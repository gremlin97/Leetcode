class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(r, c):
            if r>len(grid)-1 or c>len(grid[0])-1 or r<0 or c<0 or grid[r][c]!="1":
                return
            
            grid[r][c] = "-1"
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            
            for a,b in directions:
                dfs(r+a, c+b)
                
        count = 0
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r,c)
                    count += 1
        
        return count
                    
                        

    
            
                    
        