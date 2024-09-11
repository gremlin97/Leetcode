class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        
        adj  = defaultdict(list)
        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        
        def dfs(i, prev):
            if i not in visited:
                visited.add(i)
                
                for ne in adj[i]:
                    if ne != prev:
                        if not dfs(ne, i): return False
                    
                return True
            else:
                return False
        
        if not dfs(0,-1):
            return False
        if len(visited) != n:
            return False
        return True
        
            
        