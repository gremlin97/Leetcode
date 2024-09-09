from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        state = [0]*n
        order = []
        
        adj = defaultdict(list)
        for c,p in prerequisites:
            adj[c].append(p)
        
        # print(adj)
        
        unvisited, visiting, visited = 0, 1, 2
                
        def dfs(i):
            if state[i] == visited:
                return True
            if state[i] == visiting:
                return False
            state[i] = visiting
            
            for neigh in adj[i]:
                if not dfs(neigh):
                    return False
            
            state[i] = visited
            order.append(i)
            return True
                
        for i in range(n):
            if not dfs(i):
                return []
        return order
            
            
        