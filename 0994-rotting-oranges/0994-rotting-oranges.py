from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        m = 0  # Start counting minutes from 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i,j])
                
        while q:
            for _ in range(len(q)):
                node = q.pop(0)
                for d in directions:
                    new_x, new_y = node[0] + d[0], node[1] + d[1]
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        q.append([new_x, new_y])
            
            # Counting minutes
            m += 1
            
        # Checking if there are still fresh oranges left
        if 1 not in sum(grid, []):
            return max(0, m - 1)  # Return m - 1 because the last minute doesn't count if there are no fresh oranges
        else:
            return -1
