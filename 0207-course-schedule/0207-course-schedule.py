class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {i:[] for i in range(numCourses)}
        for cr,  pr in prerequisites:
            d[cr].append(pr)
            
        visited = set()
        def dfs(cr):
            if cr in visited:
                return False
            
            if d[cr] == []:
                return True
            
            visited.add(cr)
            for c in d[cr]:
                if not dfs(c): return False
                
            d[cr] = []
            visited.remove(cr)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True
        