class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = []
        rows = len(rooms)
        cols = len(rooms[0])
        
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append([r, c])
        
        dr = [[0,1],[0,-1],[1,0],[-1,0]]
        d = 0
        while q:
            d += 1
            for _ in range(len(q)):
                
                r, c = q.pop(0)
                
                for a, b in dr:
                    ta = (r + a)
                    tb = (c + b)
                    if 0<=ta<rows and 0<=tb<cols and d<rooms[ta][tb]:
                        rooms[ta][tb] = d
                        q.append([ta, tb])
                        
                # print(rooms,'\n')
        
        
                        
                        
                
                
                
                
                
                
        