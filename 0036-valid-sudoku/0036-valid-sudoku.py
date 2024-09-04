class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()
        ns = ['1','2','3','4','5','6','7','8','9','.']
        
        # row
        for i in range(9):
            s.clear()
            for j in range(9):
                if board[i][j] in s or board[i][j] not in ns:
                    return False
                if board[i][j] != '.':
                    s.add(board[i][j])
        
        #col
        for i in range(9):
            s.clear()
            for j in range(9):
                if board[j][i] in s or board[j][i] not in ns:
                    return False
                if board[j][i] != '.':
                    s.add(board[j][i])
        
        
        for k in range(0,7,3):
            for l in range(0,7,3):
                s.clear()
                for i in range(3):
                    for j in range(3):
                        # print(k,l)
                        # print(i+k,j+l,s)
                        if board[i+k][j+l] in s or board[i+k][j+l] not in ns:
                            return False
                        if board[i+k][j+l] != '.':
                            s.add(board[i+k][j+l])
        
        return True
                
            
            
        