# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lca(root):
            if not root:
                return None
            
            if root == p or root == q:
                return root
            
            l = lca(root.left)
            r = lca(root.right)
            
            if l and r:
                return root
            elif l:
                return l
            else:
                return r
        
        return lca(root)