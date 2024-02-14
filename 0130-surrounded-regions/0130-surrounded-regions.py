class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def fill(r,c):
            if r>len(board)-1 or c>len(board[0])-1 or r<0 or c<0 or board[r][c] == "O" or board[r][c] == "X":
                return
            
            board[r][c] = "O"
            
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            
            for a,b in directions:
                fill(r+a, c+b)
                
        for r in range(len(board)): 
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "-"
        
        for x in range(len(board[0])):
            print(0,x)
            fill(0,x)
        
        for x in range(len(board[0])):
            print(len(board)-1,x)
            fill(len(board)-1,x)
            
        for x in range(1, len(board)-1):
            print(x,0)
            fill(x,0)
        
        for x in range(1,len(board)-1):
            print(x,len(board)-1)
            fill(x,len(board[0])-1)
        
        print(board)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "-":
                    board[r][c] = "X"
            
        return board
            
            
                
                