class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = max(sum(edges, []))
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        
        def find(x):
            if parent[x] == x:
                return x
            else:
                parent[x] = find(parent[x])
                return parent[x]
        
        def union(x,y):
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return True
            else:
                if rank[p1] > rank[p2]:
                    parent[p2] = p1
                    rank[p2] += rank[p1]
                else:
                    parent[p1] = p2
                    rank[p1] += rank[p2]
            return False
        
        
        for a,b in edges:
            if union(a-1,b-1):
                return [a,b]