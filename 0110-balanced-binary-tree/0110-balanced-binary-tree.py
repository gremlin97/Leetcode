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
            nonlocal isBalanced
            
            if not r:
                return 0
            
            le = recur(r.left) + 1
            ri = recur(r.right) + 1
            
            if abs(le-ri)>1: isBalanced = False
            
            return max(le,ri)
        
        recur(root)
        return isBalanced
        