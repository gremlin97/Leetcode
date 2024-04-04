# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lca(r, p, q):
            if not r:
                return None
            if r == p or r == q:
                return r
            
            left = lca(r.left, p, q)
            right = lca(r.right, p, q)
            
            if left and right:
                return r
            elif left:
                return left
            else:
                return right
            
        return lca(root, p, q)