class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        visited = set()
        res = 0
        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        
        def dfs(i):
            if i not in visited:
                visited.add(i)
                
                for n in adj[i]:
                    dfs(n)
                return
            else:
                return
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        
        return res
                
        
        