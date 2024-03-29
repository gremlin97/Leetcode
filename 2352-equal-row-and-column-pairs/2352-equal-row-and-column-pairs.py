class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        r = {}
        c = {}
        
        for i, x in enumerate(grid):
            if i not in r:
                r[i] = x
        
        for i in range(len(grid[0])):
            temp = []
            for j in range(len(grid)):
                temp.append(grid[j][i])
            if i not in c:
                c[i] = temp
        
        res = 0
        for x in r.values():
            for y in c.values():
                if x == y:
                    res += 1
        return res
            
        
            
        
        
        
        