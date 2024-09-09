class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pf = set()
        alt = set()
        rows = len(heights)
        cols = len(heights[0])
        res = []
        
        d = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def dfs(r,c,prev,s):
            if 0<=r<rows and 0<=c<cols and heights[r][c] >= prev and (r,c) not in s:
                s.add((r,c))
                
                for a, b in d:
                    dfs(r+a,c+b,heights[r][c],s)
            else:
                return
        
        # for r in range(rows):
        #     for c in range(cols):
        #         if r == 0 or c == 0:
        #             dfs(r,c,heights[r][c],pf)
        #         elif r == rows-1 or c == cols - 1::
        #             dfs(r,c,heights[r][c],alt)
        
        for r in range(rows):
            dfs(r,0,heights[r][0],pf)
            dfs(r,cols-1,heights[r][cols-1],alt)
            
        for c in range(cols):
            dfs(0,c,heights[0][c],pf)
            dfs(rows-1,c,heights[rows-1][c],alt)

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pf and (r,c) in alt:
                    res.append([r,c])
        
        return res
                    
        
                    
                    