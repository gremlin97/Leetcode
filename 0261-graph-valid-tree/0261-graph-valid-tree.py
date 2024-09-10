class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visited = set()
        res = 0
        
        for c, p in edges:
            adj[c].append(p)
            adj[p].append(c)
            
        def dfs(i, prev):
            if i not in visited:
                visited.add(i)
                
                for n in adj[i]:
                    if n == prev:
                        continue
                    if not dfs(n, i):
                        return False
                return True
            else:
                return False
        

        if not dfs(0, -1):
            return False
        
        if len(visited) != n: return False
        
        return True
                