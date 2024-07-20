# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(r):
            if not r:
                return
            t = r.left
            r.left = r.right
            r.right = t
            invert(r.left)
            invert(r.right)
        
        invert(root)
        return root
            
        