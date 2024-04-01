class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = []
        q.append([entrance[0], entrance[1]])
        level = 0
        d = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = set()
        visited.add((entrance[0], entrance[1]))
        
        while(q):
            for _ in range(len(q)):
                cell = q.pop(0)
                
                if maze[cell[0]][cell[1]] == '.' and ((cell[0] == (len(maze) - 1) or cell[0] == 0) or (cell[1] == len(maze[0]) - 1 or cell[1] == 0)) and (cell[0],cell[1]) != (entrance[0], entrance[1]):
                    return level
                
                for x in d:
                    if (cell[0] + x[0] < len(maze) and (cell[0] + x[0] >=0)) and cell[1] + x[1] < len(maze[0]) and cell[1] + x[1] >=0 and (maze[cell[0] + x[0]][cell[1] + x[1]] == '.' and (cell[0] + x[0], cell[1] + x[1]) not in visited):
                        visited.add((cell[0] + x[0], cell[1] + x[1]))
                        q.append([cell[0] + x[0], cell[1] + x[1]])
            level += 1
                        
        return -1
                
                
                
            
            
    
        