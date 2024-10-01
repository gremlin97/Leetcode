# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        def recur(r):
            if not r:
                return 0
            
            l = recur(r.left) + 1
            r = recur(r.right) + 1
            
            if abs(l-r)>1:
                self.isBalanced = False
            
            return max(l,r)
        
        recur(root)
        return self.isBalanced
        
    
            
            
            
        