class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        d = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        
        def dfs(r,c,i):
            if i == len(word):
                return True
            
            if r<0 or c<0 or r>rows-1 or c>cols-1 or (r,c) in visited:
                return False
            
            if word[i] != board[r][c]:
                return False
            
            visited.add((r,c))
            res = False
            for a, b in d:
                res = res or dfs(r+a, c+b, i+1)
            
            visited.remove((r,c))
            
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0): return True
        
        return False
        