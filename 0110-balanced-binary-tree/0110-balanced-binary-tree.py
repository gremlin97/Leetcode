# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(r):
            if not r:
                return 0
            return 1 + max(height(r.left), height(r.right))
        
        def check(r):
            if not r:
                return True
            
            lh = height(r.left)
            rh = height(r.right)
            
            return (abs(lh - rh) <= 1) and check(r.left) and check(r.right)
        
        return check(root)