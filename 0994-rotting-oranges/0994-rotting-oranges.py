class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        org = 0
        rows, cols = len(grid), len(grid[0])
        res = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
                if grid[r][c] == 1:
                    org += 1
        
        
        while q and org>0:
            dr = [[0,1],[0,-1],[1,0],[-1,0]]
            for _ in range(len(q)):
                n = q.pop(0)
                
                for a, b in dr:
                    nr, nc = n[0]+a, n[1]+b
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append([nr, nc])
                        org -= 1
                        print(grid)
            res += 1
        
        print(res, org, grid)
        
        if org == 0:
            return res
        return -1
                
            
                
            