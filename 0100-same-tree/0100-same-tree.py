# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        def recur(p,q):
            
            if not p and not q:
                return True
            
            if p and not q:
                return False
            
            if not p and q:
                return False
            
            if p.val == q.val:
                return recur(p.left, q.left) and recur(p.right, q.right)
            else:
                return False
                
        return recur(p, q)
            
            