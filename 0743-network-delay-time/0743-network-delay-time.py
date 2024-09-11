class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        t = 0
        q = [(0,k)]
        visited = set()
        
        adj = {i:[] for i in range(1,n+1)}
        for a,b,c in times:
            adj[a].append([b,c])
        
        while q:
            size = len(q)
            for _ in range(size):
                w1, n1 = heapq.heappop(q)

                if n1 not in visited:
                    visited.add(n1)
                    t = max(t,w1)

                    for n2,w2 in adj[n1]:
                        if n2 not in visited:
                            heapq.heappush(q,(w1+w2, n2))

        print(visited, n)
        if len(visited) == n:
            return t
        return -1
            
                        
                        
                
                
        
        