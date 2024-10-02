# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(a, b):
            if not a and not b:
                return True
            if (not a and b) or (not b and a):
                return False
            
            if a.val == b.val:
                return same(a.left, b.left) and same(a.right, b.right)
            else:
                return False
            
            
        def isSubtree(r):
            if not r:
                return 
            return same(r, subRoot) or isSubtree(r.left) or isSubtree(r.right)
        
        return isSubtree(root)
        