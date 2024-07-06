class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        
        def dfs(r, c):
            
            if 0<=r<len(grid) and 0<=c<len(grid[0]):
                if grid[r][c] == '1': 

                    grid[r][c] = '-1'

                    trav = [[0,1],[0,-1],[1,0],[-1,0]]

                    for x,y in trav:
                        dfs(r+x, c+y)

                        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    dfs(r,c)
                    res += 1
        
        return res
                    
            
            
        