# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lca(root, p, q):
            if root == p or root == q or root == None:
                return root
            
            ls = lca(root.left,p,q)
            rs = lca(root.right,p,q)

            if ls and rs:
                return root
            if ls:
                return ls
            return rs
        
        return lca(root, p, q)
        
        
        