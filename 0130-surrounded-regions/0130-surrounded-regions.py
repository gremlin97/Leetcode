class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        d = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def dfs(r, c):
            # print(r,c)
            if 0<=r<=(len(board)-1) and 0<=c<=(len(board[0])-1) and board[r][c] == 'O':
                board[r][c] = '-'
                for a,b in d:
                    dfs(r+a, c+b)
            else:
                return
            
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (board[r][c] == 'O') and (r in (0,len(board)-1) or c in (0, len(board[0])-1)):
                    print(r,c)
                    dfs(r,c)
                    
        # print(board)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '-':
                    board[r][c] = 'O'
                    continue
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                
    
                
        
        
        