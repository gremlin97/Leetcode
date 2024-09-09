class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = {}
        res = 0
        
        adj = {i:[] for i in range(n)}
        for i, t in edges:
            adj[i].append(t)
            adj[t].append(i)
            
        
        print(adj)
        
        def dfs(n):
            if n not in visited:
                visited.add(n)
            
                for x in adj[n]:
                    dfs(x)
            return 
                
        
        for k in adj.keys():
            if k not in visited:
                dfs(k)
                res += 1
        
        return res
        
        
    
                
                
                
        