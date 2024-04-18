class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        res = 0
        
        def neigh(r,c):
            n = 0
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for x,y in directions:
                if 0<=(r+x)<len(grid) and 0<=(c+y)<len(grid[0]):
                    if grid[r+x][c+y] == 1:
                        n+=1
            return n
        
#         def dfs(r,c):
#             if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c] == 1 and(r,c) not in visited:
#                 visited.add((r,c))
#                 grid[r][c] = -1
#                 directions = [[1,0],[-1,0],[0,1],[0,-1]]
#                 for x,y in directions:
#                     dfs(r+x,c+y)
#             else:
#                 return
        
#         for a in range(len(grid)):
#             for b in range(len(grid[0])):
#                 dfs(a,b)
        
        for a in range(len(grid)):
            for b in range(len(grid[0])):
                if grid[a][b] == 1:
                    t = neigh(a,b)
                    print(a,b,t)
                    res = res + (4-t)
                
        print(neigh(0,1))
        
        return res
                    
                    
                    
        
        
                
                
        