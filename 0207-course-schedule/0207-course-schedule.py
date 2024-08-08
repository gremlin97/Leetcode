class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {i:[] for i in range(numCourses)}
        
        for course, pre in prerequisites:
            d[course].append(pre)
        
        visited = set()
        def dfs(i):
            if i in visited:
                return False
            if d[i] == []:
                return True
            
            visited.add(i)
            
            for course in d[i]:
                if not dfs(course):
                    return False
            
            d[i] = []
            visited.remove(i)
            
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True
    
            
            
            
            
        