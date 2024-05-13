class Solution:
    def count(self, grid, c):
        c0, c1 = 0, 0
        for r in range(len(grid)):
            # print(grid[r][c],r,c)
            if grid[r][c] == 1:
                c1 += 1
            else:
                c0 += 1
            
        # print(c0, c1)
        if c0 > c1:
            return True
        return False
        
    def matrixScore(self, grid: List[List[int]]) -> int:
        for r in range(len(grid)):
            if grid[r][0] != 1:
                for c in range(len(grid[0])):
                    grid[r][c] = grid[r][c] ^ 1
        
        # print(grid)
        # print('Count', self.count(grid,2))
        
        for c in range(len(grid[0])):
            if self.count(grid, c):
                for r in range(len(grid)):
                    grid[r][c] = grid[r][c] ^ 1
                    
        # print(grid)
        s = 0
        for r in range(len(grid)):
            temp = ''
            for c in range(len(grid[0])):
                # print(grid[r][c])
                temp += str(grid[r][c])
                # print(temp)
            s += int(temp,2)
        
        return s
        