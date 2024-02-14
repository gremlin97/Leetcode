class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        org = image[sr][sc]
        
        def floodFillUtil(r, c, fillcolor):
            if r>(len(image)-1) or c>(len(image[0])-1) or r<0 or c<0 or image[r][c] == color or image[r][c] != fillcolor:
                return
            
            image[r][c] = color
            directions = [[1,0],[-1,0],[0,-1],[0,1]]
            
            for a, b in directions:
                floodFillUtil(r+a, c+b, org)
                
        floodFillUtil(sr,sc, org)
        
        return image
                
        
        