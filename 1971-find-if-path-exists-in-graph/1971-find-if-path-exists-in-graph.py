class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        start = source
        end = destination
        neighbors = defaultdict(list)
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)
            
        def dfs(node, end, seen):
            if node == end:
                return True
            if node in seen:
                return False
            
            seen.add(node)
            for n in neighbors[node]:
                if dfs(n, end, seen):
                    return True
                
            return False
        
        seen = set()    
        return dfs(start, end, seen)
        