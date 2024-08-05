# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        pg = []
        res = 0
        
        def paths(r, p):
            if not r:
                return 
            
            p.append(r.val)
            temp = p.copy()
            
            pg.append(p.copy())
            paths(r.left, p)
            paths(r.right, temp)
            
        paths(root,[])
        
        for p in pg:
            if p[len(p)-1] == max(p):
                res += 1
        
        return res
                
            
        