class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(x,y,w):
            if w[0] != board[x][y]:
                return False
        
            if len(w) == 1:
                # print('Final Letter is:',w[0])
                return True
            
            visited.add((x,y))
            
            # print(visited)
            # print(board[x][y])
            # print("Word",w)
        
            dr = [[0,1],[0,-1],[1,0],[-1,0]]
            for d in dr:
                new_x = x + d[0] 
                new_y = y + d[1]
                
                o_r = False
                if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and (new_x,new_y) not in visited:
                    if dfs(new_x, new_y, w[1:]):
                        # print('Here')
                        return True
            visited.remove((x,y))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,word):
                    return True
                visited.clear()
        return False

            
        