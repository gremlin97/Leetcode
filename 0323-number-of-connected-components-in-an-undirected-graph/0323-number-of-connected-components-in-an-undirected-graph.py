class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)] 
        rank = [1] * (n)
        
        
        def find(x):
            if parent[x] != x:
                res = find(parent[x])
                return res
            return parent[x]
        
        def union(x,y):
            p1, p2 = find(a), find(b)
            
            if p1 == p2:
                return False
            else:
                if rank[p1]>rank[p2]:
                    parent[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    parent[p1] = p2
                    rank[p2] += rank[p1]
            return True
        
        res = n
        for a,b in edges:
            if union(a,b):
                res -= 1
        
        return res
                
        
        
        