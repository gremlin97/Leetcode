class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        m = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i,j])
                
        while(q):
            for _ in range(len(q)):
                node = q.pop(0)
                for d in directions:
                    new_x = node[0] + d[0]
                    new_y = node[1] + d[1]
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                        if grid[new_x][new_y] == 1:
                            grid[new_x][new_y] = 2
                            q.append([new_x,new_y])
            m += 1
            
        if 1 not in sum(grid,[]):
            return max(0,m-1)
        else:
            return -1
            
                        
                    
                
            