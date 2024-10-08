class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {i:[] for i in range(numCourses)}
        
        for a,b in prerequisites:
            d[a].append(b)
        visited = set()
        
        def dfs(i):
            if i not in visited:
                visited.add(i)
                for ne in d[i]:
                    if not dfs(ne):
                        return False
                d[i] = []
                visited.remove(i)
                return True
            else:
                return False
        
        for x in range(numCourses):
            if not dfs(x):
                return False
        return True
    
            
            
        
        