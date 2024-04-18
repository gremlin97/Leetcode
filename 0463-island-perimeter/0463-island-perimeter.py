class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        
        def neigh(r,c):
            n = 0
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for x,y in directions:
                if 0<=(r+x)<len(grid) and 0<=(c+y)<len(grid[0]):
                    if grid[r+x][c+y] == 1:
                        n+=1
            return n
        
        for a in range(len(grid)):
            for b in range(len(grid[0])):
                if grid[a][b] == 1:
                    t = neigh(a,b)
                    res = res + (4-t)
        
        return res
                    
                    
                    
        
        
                
                
        