class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(r, v):
            if r[v] == []:
                r[v] = ['v']
            for i in range(len(r[v])):
                key = r[v][i]
                if key != 'v':
                    r[v][i] = 'v'
                    dfs(r, key)
        
        dfs(rooms, 0)
        rooms = sum(rooms,[])
        for x in rooms:
            if x != 'v':
                return False
        return True
                
            
            
        