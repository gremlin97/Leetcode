# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lca(root, a, b):
            if not root:
                return None
            if root == a or root == b: return root
            
            l = lca(root.left, a, b)
            r = lca(root.right, a , b)
            
            if l and r:
                return root
            if l:
                return l
            return r
        
        return lca(root, p, q)