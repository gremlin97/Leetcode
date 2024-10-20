"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        def get_parent(p):
            if p.parent is None:
                return p
            return get_parent(p.parent)
        
        root = get_parent(p)
            
        
        def lca(root, p, q):
            if not root:
                return 
            
            if root == p or root == q:
                return root
            
            l = lca(root.left, p, q)
            r = lca(root.right, p , q)
            
            if l and r: return root
            if l: return l
            return r
        
        return lca(root, p, q)
            
            
                
        