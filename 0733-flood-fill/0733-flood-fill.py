class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]:
            return image
        
        rows = len(image)
        cols = len(image[0])
        
        curr = image[sr][sc]
        dr = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def fill(r, c):
            if 0<=r<rows and 0<=c<cols and image[r][c] == curr:
                image[r][c] = color
                
                for a,b in dr:
                    fill(r+a, c+b)

            else:
                return
        
        fill(sr,sc)
        return image
        
        