class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        
        for a,b in prerequisites:
            adj[a].append(b)
            
        unvisited, visiting, visited = 0, 1, 2
        
        state = [0 for i in range(numCourses)]
        
        def dfs(i):
            if state[i] == visited: return True
            elif state[i] == visiting: return False
            else:
                state[i] = 1
                
                for n in adj[i]:
                    if not dfs(n):
                        return False
                
                adj[i] = []
                state[i] = 2
                return True
        
        for x in range(numCourses):
            if not dfs(x):
                return False
        return True
    
            
            
        
        