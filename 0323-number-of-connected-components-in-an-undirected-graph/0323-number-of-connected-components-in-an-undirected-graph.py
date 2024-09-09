# class UnionFind: 
#     def __init__(self, n):
#         self.parent = list(range(n))
#         self.rank = [1]*n
#         self.components = n
    
#     def find(self, p):
#         if p != self.parent[p]: 
#             self.parent[p] = self.find(self.parent[p])
#         return self.parent[p]
    
#     def union(self, p, q):
#         prt, qrt = self.find(p), self.find(q)
#         if prt == qrt: return False 
#         self.components -= 1
#         if self.rank[prt] > self.rank[qrt]: prt, qrt = qrt, prt
#         self.parent[prt] = qrt
#         self.rank[qrt] += self.rank[qrt]
#         return True 
    

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges: uf.union(u, v)
        return uf.components
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1 for i in range(n)]
        
        def find(node):
            if par[node] == node:
                return node
            # par[node] = find(par[node])
            # return par[node]
            temp = find(par[node])
            print(node, "'s par ", temp)
            return temp
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # print("before ", par)
            # print(n1, "union",n2)
            if p1 == p2:
                return
            else:
                # have to merge it 
                if rank[p1] < rank[p2]:
                    par[p1] = p2
                    rank[p2] += rank[p1]
                else:
                    par[p2] = p1
                    rank[p1] += rank[p2]
            # print("after", par)
                
        
        ans = n
        # tt = set()
        # for node in range(n):
            
        for u,v in edges:
            paru, parv = par[u], par[v]
            # tt.add(u)
            # tt.add(v)
            # print(par)
            # print(paru, parv)
            if paru != parv:
                union(u, v)
                # ans -= 1
                print('Curr ans:', ans)
        # print("final", ans)
        # # return ans + n - len(tt)
        # return ans
        ans = 0
        for i in range(n):
            if par[i] == i:
                ans += 1
        # print('Parent:',par)
        return ans